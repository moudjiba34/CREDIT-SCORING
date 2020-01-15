def predict(client_id=None, new_client_data=None):  
    import pandas as pd
    import numpy as np
    from warnings import simplefilter
    simplefilter(action='ignore')

    if client_id is not  None:
        data=pd.read_csv("Test_base.csv",sep=";",encoding="ISO-8859-1")
       ## data =data.drop(['E2_EtudeDemandePret'],axis=1)
    #     get the index of the user 
        
    
        index = np.where(data['ID']==client_id)
        index = index[0][0]
        client_data = data.iloc[[index]]
    elif new_client_data is not None:
        client_data = new_client_data
    else:
        return "You must pass either an id of client or the data of a new client"
        
        
    #client_data['Montant']=client_data['Montant'].apply(lambda x: x.translate({0xa0:''}))
    client_data['Taux']=float(client_data['Taux'])
    client_data['DNA']=pd.to_datetime(client_data['DNA'])

    client_data['year_DAN']=client_data['DNA'].dt.year
    client_data['age_cli']=2019-client_data['year_DAN']

    client_data["Typrt_Crédits Immobiliers : PPI 1 PPI 2 pour les acquisitions de biens immobiliers: terrain, villa, immeubles"] = np.where(client_data["Typrt"] == "Crédits Immobiliers : PPI 1 PPI 2 pour les acquisitions de biens immobiliers: terrain, villa, immeubles",1,0)[0]
    client_data["Typrt_Crédits Immobiliers : PPI 1 PPI 2 pour les constructions, transformations ou finitions"] =  np.where(client_data["Typrt"] == "Crédits Immobiliers : PPI 1 PPI 2 pour les constructions, transformations ou finitions" ,1,0)[0]
    client_data["Typrt_Crédits de Consommation : PPE PPO PPMTS"] =  np.where (client_data["Typrt"] == "Crédits de Consommation : PPE PPO PPMTS",1,0)[0]

    client_data["RYTHREM_Mensuel"] = np.where(client_data["RYTHREM"] == "Mensuel" ,1,0)[0]
    client_data["RYTHREM_Trimestriel"] = np.where (client_data["RYTHREM"] == "Trimestriel",1,0)[0]
    client_data["AUTGAR_False"] = np.where(client_data["AUTGAR"] == "False" ,1,0)[0]
    client_data["AUTGAR_True"] = np.where(client_data["AUTGAR"] == "True" ,1,0)[0]
    
    if client_id is not  None:
        x=client_data.drop(['ID_INSTANCE_WORKFLOW','Etat','ID','NOMCLIENT','RYTHREM','AUTGAR','Typrt','Initiateur','year_DAN','Date_DerniereExecution'
                        ,'DMO','DNA','DATDMDE','ContentType','Status','EtatInterne','LibelleItem'],axis=1)
    elif new_client_data is not None:
        x=client_data.drop(['RYTHREM','AUTGAR','Typrt','year_DAN','DNA'],axis=1)
    
    # Load the model and make the prediction
    from sklearn.externals import joblib
    # load the model 
    model= joblib.load('classification1.sav') 
    predictions=model.predict(x)
    submission=pd.DataFrame({'ID' :client_data['ID'],'Montant':client_data['Montant'],'Taux':client_data['Taux'],'DUR_REMB':client_data['DUR_REMB'],'Typrt':client_data['Typrt'],'resultat':predictions})
    filename='scoring.xlsx'
    submission.to_excel(filename,index=False)
    if predictions[0]==1:
        return 'pret a accepter'
    else:
      return 'pret a refuser'
       
  
