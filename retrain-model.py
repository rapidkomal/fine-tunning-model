#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import os

df = pd.read_csv("/Users/komal/downloads/questions-list-1.csv")
df.head()


# In[6]:


df = df.iloc[:, :2]


# In[7]:


new_names = {'Question': 'prompt', 'Answer': 'completion'}
df = df.rename(columns=new_names)


# In[8]:


df


# In[9]:


data = [{"prompt": "Create a technical specification document for a new website. The document should detail the technical requirements, architecture, and design of the website.", "completion": "Introduction:\n\nThe purpose of this technical specification document is to outline the technical requirements, architecture, and design for a new website.\n\nRequirements:\n\nFunctional Requirements:\n- The website must be able to display pages in multiple languages.\n- The website must have a contact form for users to submit inquiries.\n\nNon-functional Requirements:\n- The website must have a load time of less than 3 seconds.\n- The website must be accessible to users with disabilities.\n\nArchitecture:\n\nThe website will be built using a LAMP stack. The following components will be used:\n- Apache web server\n- MySQL database\n- PHP scripting language\n\nDesign:\n\nThe website will be designed using the following principles:\n- Principle A: description\n- Principle B: description\n\nTesting:\n\nThe website will be tested using the following methods:\n- Unit testing: description\n- Integration testing: description\n- User acceptance testing: description\n\nDeployment:\n\nThe website will be deployed to the following environments:\n- Development environment: description\n- Testing environment: description\n- Production environment: description\n\nMaintenance:\n\nThe following maintenance tasks will be required for the website:\n- Task A: description\n- Task B: description\n\nConclusion:\n\nThis technical specification document provides a detailed overview of the technical requirements, architecture, and design for the new website. It will serve as a reference for the development and maintenance of the website."},
{"prompt": "Create a technical specification document for a new mobile app. The document should detail the technical requirements, architecture, and design of the mobile app.", "completion": "Introduction:\n\nThe purpose of this technical specification document is to outline the technical requirements, architecture, and design for a new mobile app.\n\nRequirements:\n\nFunctional Requirements:\n- The mobile app must be able to display content in real-time.\n- The mobile app must have a user login and registration system.\n\nNon-functional Requirements:\n- The mobile app must have a load time of less than 1 second.\n- The mobile app must be compatible with iOS and Android devices.\n\nArchitecture:\n\nThe mobile app will be built using a native approach for each platform. The following components will be used:\n- iOS: Swift programming language, Xcode IDE\n- Android: Java programming language, Android Studio IDE\n\nDesign:\n\nThe mobile app will be designed using the following principles:\n- Principle A: description\n- Principle B: description\n\nTesting:\n\nThe mobile app will be tested using the following methods:\n- Unit testing: description\n- Integration testing: description\n- User acceptance testing: description\n\nDeployment:\n\nThe mobile app will be deployed to the following app stores:\n- Apple App Store\n- Google Play Store\n\nMaintenance:\n\nThe following maintenance tasks will be required for the mobile app:\n- Task A: description\n- Task B: description\n\nConclusion:\n\nThis technical specification document provides a detailed overview of the technical requirements, architecture, and design for the new mobile app. It will serve as a reference for the development and maintenance of the mobile app."},
{"prompt": "Create an architectural overview document for a new cloud-based software system. The document should include an overview of the system architecture and its components.", "completion": "Introduction:\n\nThe purpose of this architectural overview document is to provide a high-level overview of the architecture of a new cloud-based software system. This document outlines the various components of the system and their interactions.\n\nSystem Architecture:\n\nThe software system will be built using a microservices architecture. The system will consist of the following components:\n\n- Authentication Service: This component will handle user authentication and authorization.\n- API Gateway: This component will serve as a front-end for all incoming requests.\n- User Service: This component will handle user-related operations.\n- Product Service: This component will handle product-related operations.\n- Order Service: This component will handle order-related operations.\n\nInteraction Between Components:\n\nThe components of the system will interact with each other through APIs. The API Gateway will be responsible for routing requests to the appropriate service. The services will communicate with each other through REST APIs.\n\nConclusion:\n\nThis architectural overview document provides an overview of the system architecture and its components. It will serve as a reference for the development and maintenance of the software system."},
{"prompt": "Create a design document for a new mobile application. The document should detail the architecture of the application and its components.", "completion": "Introduction:\n\nThe purpose of this design document is to outline the architecture of a new mobile application. This document provides a detailed description of the various components of the application and their interactions.\n\nSystem Architecture:\n\nThe mobile application will be built using a client-server architecture. The application will consist of the following components:\n\n- Client: This component will be the user interface of the application.\n- Server: This component will handle all the business logic and data management.\n\nInteraction Between Components:\n\nThe client will communicate with the server through REST APIs. The server will store data in a database and retrieve data from it as needed. The server will also be responsible for authenticating and authorizing users.\n\nConclusion:\n\nThis design document provides an overview of the architecture of the mobile application and its components. It will serve as a reference for the development and maintenance of the application."},
{"prompt": "Create a technical specification document for a new web application. The document should detail the architecture and design of the application.", "completion": "Introduction:\n\nThe purpose of this technical specification document is to outline the architecture and design of a new web application. This document provides a detailed description of the various components of the application and their interactions.\n\nSystem Architecture:\n\nThe web application will be built using a three-tier architecture. The application will consist of the following components:\n\n- Presentation Tier: This component will be responsible for handling user input and output. It will be implemented using HTML, CSS, and JavaScript.\n- Application Tier: This component will handle all the business logic and data management. It will be implemented using Java and the Spring framework.\n- Data Tier: This component will be responsible for storing and retrieving data. It will be implemented using a MySQL database.\n\nInteraction Between Components:\n\nThe presentation tier will communicate with the application tier through REST APIs. The application tier will communicate with the data tier through JDBC. The application tier will also be responsible for authenticating and authorizing users.\n\nDesign:\n\nThe web application will be designed using a responsive design approach."},
{"prompt": "Create a design document for a new mobile application. The document should detail the architecture of the application and its components.", "completion": "Introduction:\n\nThe purpose of this design document is to outline the architecture of a new mobile application. This document provides a detailed description of the various components of the application and their interactions.\n\nSystem Architecture:\n\nThe mobile application will be built using a client-server architecture. The application will consist of the following components:\n\n- Client: This component will be the user interface of the application.\n- Server: This component will handle all the business logic and data management.\n\nInteraction Between Components:\n\nThe client will communicate with the server through REST APIs. The server will store data in a database and retrieve data from it as needed. The server will also be responsible for authenticating and authorizing users.\n\nConclusion:\n\nThis design document provides an overview of the architecture of the mobile application and its components. It will serve as a reference for the development and maintenance of the application."},
{"prompt": "Create a technical specification document for a new web application. The document should detail the architecture and design of the application.", "completion": "Introduction:\n\nThe purpose of this technical specification document is to outline the architecture and design of a new web application. This document provides a detailed description of the various components of the application and their interactions.\n\nSystem Architecture:\n\nThe web application will be built using a three-tier architecture. The application will consist of the following components:\n\n- Presentation Tier: This component will be responsible for handling user input and output. It will be implemented using HTML, CSS, and JavaScript.\n- Application Tier: This component will handle all the business logic and data management. It will be implemented using Java and the Spring framework.\n- Data Tier: This component will be responsible for storing and retrieving data. It will be implemented using a MySQL database.\n\nInteraction Between Components:\n\nThe presentation tier will communicate with the application tier through REST APIs. The application tier will communicate with the data tier through JDBC. The application tier will also be responsible for authenticating and authorizing users.\n\nDesign:\n\nThe web application will be designed using a responsive design approach"},
{"prompt": "Create a technical design document for a new e-commerce website. The document should detail the architecture and design of the website.", "completion": "Introduction:\n\nThe purpose of this technical design document is to outline the architecture and design of a new e-commerce website. This document provides a detailed description of the various components of the website and their interactions.\n\nSystem Architecture:\n\nThe e-commerce website will be built using a client-server architecture. The website will consist of the following components:\n\n- Client: This component will be the user interface of the website. It will be implemented using HTML, CSS, and JavaScript.\n- Server: This component will handle all the business logic and data management. It will be implemented using Java and the Spring framework.\n- Database: This component will be responsible for storing and retrieving data. It will be implemented using a MySQL database.\n\nInteraction Between Components:\n\nThe client will communicate with the server through REST APIs. The server will store data in a database and retrieve data from it as needed. The server will also be responsible for authenticating and authorizing users.\n\nDesign:\n\nThe e-commerce website will be designed to be user-friendly and easy to navigate. The website will include features such as a shopping cart, search functionality, and user profiles. The website will be optimized for performance and scalability.\n\nConclusion:\n\nThis technical design document provides an overview of the architecture and design of the e-commerce website. It will serve as a reference for the development and maintenance of the website."},
{"prompt": "Create an architecture document for a new cloud-based CRM system. The document should detail the system architecture and its components.", "completion": "Introduction:\n\nThe purpose of this architecture document is to provide an overview of the architecture of a new cloud-based CRM system. This document outlines the various components of the system and their interactions.\n\nSystem Architecture:\n\nThe CRM system will be built using a microservices architecture. The system will consist of the following components:\n\n- Authentication Service: This component will handle user authentication and authorization.\n- API Gateway: This component will serve as a front-end for all incoming requests.\n- Customer Service: This component will handle customer-related operations.\n- Sales Service: This component will handle sales-related operations.\n- Marketing Service: This component will handle marketing-related operations.\n\nInteraction Between Components:\n\nThe components of the system will interact with each other through APIs. The API Gateway will be responsible for routing requests to the appropriate service. The services will communicate with each other through REST APIs.\n\nConclusion:\n\nThis architecture document provides an overview of the system architecture and its components. It will serve as a reference for the development and maintenance of the CRM system."},
{"prompt": "Create a technical specification document for a new online education platform. The document should detail the architecture and design of the platform.", "completion": "Introduction:\n\nThe purpose of this technical specification document is to outline the architecture and design of a new online education platform. This document provides a detailed description of the various components of the platform and their interactions.\n\nSystem Architecture:\n\nThe online education platform will be built using a client-server architecture. The platform will consist of the following components:\n\n- Client: This component will be the user interface of the platform. It will be implemented using HTML, CSS, and JavaScript.\n- Server: This component will handle all the business logic and data management. It will be implemented using Java and the Spring framework.\n- Database: This component will be responsible for storing and retrieving"},
{"prompt": "Create a technical specification document for a new mobile app that allows users to book and manage appointments with doctors. The document should detail the architecture and design of the app.", "completion": "Introduction:\n\nThe purpose of this technical specification document is to outline the architecture and design of a new mobile app that allows users to book and manage appointments with doctors. This document provides a detailed description of the various components of the app and their interactions.\n\nSystem Architecture:\n\nThe mobile app will be built using a client-server architecture. The app will consist of the following components:\n\n- Client: This component will be the user interface of the app. It will be implemented using React Native.\n- Server: This component will handle all the business logic and data management. It will be implemented using Node.js and the Express framework.\n- Database: This component will be responsible for storing and retrieving data. It will be implemented using MongoDB.\n\nInteraction Between Components:\n\nThe client will communicate with the server through REST APIs."},
{"prompt": "Create a technical specification document for a new mobile app that allows users to book and manage appointments with doctors. The document should detail the architecture and design of the app.", "completion": "Introduction:\n\nThe purpose of this technical specification document is to outline the architecture and design of a new mobile app that allows users to book and manage appointments with doctors. This document provides a detailed description of the various components of the app and their interactions.\n\nSystem Architecture:\n\nThe mobile app will be built using a client-server architecture. The app will consist of the following components:\n\n- Client: This component will be the user interface of the app. It will be implemented using React Native.\n- Server: This component will handle all the business logic and data management. It will be implemented using Node.js and the Express framework.\n- Database: This component will be responsible for storing and retrieving data. It will be implemented using MongoDB.\n\nInteraction Between Components:\n\nThe client will communicate with the server through REST APIs. The server will store data in a database and retrieve data from it as needed. The server will also be responsible for authenticating and authorizing users.\n\nDesign:\n\nThe mobile app will be designed to be user-friendly and easy to navigate. The app will include features such as appointment booking, appointment management, and a doctor search functionality. The app will be optimized for performance and scalability.\n\nConclusion:\n\nThis technical specification document provides an overview of the architecture and design of the mobile app. It will serve as a reference for the development and maintenance of the app."},
{"prompt": "Create a technical specification document for a new social media platform. The document should detail the architecture and design of the platform.", "completion": "Introduction:\n\nThe purpose of this technical specification document is to outline the architecture and design of a new social media platform. This document provides a detailed description of the various components of the platform and their interactions.\n\nSystem Architecture:\n\nThe social media platform will be built using a microservices architecture. The platform will consist of the following components:\n\n- Authentication Service: This component will handle user authentication and authorization.\n- API Gateway: This component will serve as a front-end for all incoming requests.\n- User Service: This component will handle user-related operations.\n- Post Service: This component will handle post-related operations.\n- Comment Service: This component will handle comment-related operations.\n\nInteraction Between Components:\n\nThe components of the platform will interact with each other through APIs. The API Gateway will be responsible for routing requests to the appropriate service. The services will communicate with each other through REST APIs.\n\nDesign:\n\nThe social media platform will be designed to be user-friendly and easy to navigate. The platform will include features such as post sharing, commenting, and liking. The platform will be optimized for performance and scalability.\n\nConclusion:\n\nThis technical specification document provides an overview of the architecture and design of the social media platform. It will serve as a reference for the development and maintenance of the platform." },
{"prompt": "Create a technical specification document for a new chatbot that can answer questions about a product. The document should detail the architecture and design of the chatbot.", "completion": "Introduction:\n\nThe purpose of this technical specification document is to outline the architecture and design of a new chatbot that can answer questions about a product. This document provides a detailed description of the various components of the chatbot and their interactions.\n\nSystem Architecture:\n\nThe chatbot will be built using a natural language "},
{"prompt": "What is HTML?", "completion": "HTML stands for Hypertext Markup Language. It is the standard markup language used for creating web pages."},
{"prompt": "What is CSS?", "completion": "CSS stands for Cascading Style Sheets. It is a style sheet language used for describing the presentation of a document written in HTML or XML."},
{"prompt": "What is JavaScript?", "completion": "JavaScript is a high-level programming language used to create interactive web pages and web applications."},
{"prompt": "What is a database?", "completion": "A database is an organized collection of data, typically stored and accessed electronically from a computer system."},
{"prompt": "What is SQL?", "completion": "SQL stands for Structured Query Language. It is a standard language used for managing and manipulating data in relational databases."},
{"prompt": "What is Git?", "completion": "Git is a distributed version control system used for tracking changes in source code during software development."},
{"prompt": "What is REST?", "completion": "REST stands for Representational State Transfer. It is an architectural style used for building web services and APIs."},
{"prompt": "What is Docker?", "completion": "Docker is a platform used for developing, shipping, and running applications in containers."},
{"prompt": "What is DevOps?", "completion": "DevOps is a set of practices used for combining software development and IT operations to shorten the systems development life cycle."},
{"prompt": "What is cloud computing?", "completion": "Cloud computing is the delivery of computing services, including servers, storage, databases, networking, software, analytics, and intelligence, over the internet."}]
 
 


# In[14]:


new_df = pd.DataFrame(data)


# In[15]:


combined_df = pd.concat([df, new_df], ignore_index=True)


# In[17]:


combined_df.to_csv('new-questions.csv')


# In[18]:


combined_df.to_json("new-questions.jsonl", orient='records', lines=True)


# In[ ]:





# In[23]:


import openai
openai.api_key = "...."
os.environ['OPENAI_API_KEY'] = openai.api_key


# In[19]:


get_ipython().system('openai tools fine_tunes.prepare_data -f new-questions.jsonl -q')


# In[38]:


get_ipython().system('openai api fine_tunes.create -t "new-questions_prepared.jsonl" -m ada:ft-personal-2023-04-25-12-00-27')


# In[58]:


get_ipython().system('openai api fine_tunes.follow -i ft-YEZPYqHYYocfWTUv9kz2mmN7')


# In[40]:


get_ipython().system('openai api fine_tunes.list')


# In[ ]:


get_ipython().system('openai api fine_tunes.results -i ft-fWMcVjVyWXUW6NTZYSN8Q00N > new-result.csv')


# In[ ]:


results = pd.read_csv('result.csv')


# In[ ]:


results.head(20)


# In[74]:


ft_model = 'ada:ft-personal-2023-04-26-07-31-36'
res = openai.Completion.create(
model=ft_model,
prompt="What is a database?",
max_tokens=250,
presence_penalty=0.2, 
temperature=0,
frequency_penalty=2
)
res['choices'][0]['text']


# In[35]:


import requests

# Read the contents of the JSONL file into a string
with open("new-questions.jsonl", "r") as f:
    dataset_str = f.read()

    
url = "https://api.openai.com/v1/fine-tunes/append"

payload = {
    "model": "ada:ft-personal-2023-04-25-12-00-27",
    "files": [
        {
            "filename": "new-questions_prepared.jsonl",
            "data": dataset_str
        }
    ]
}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"
}

response = requests.post(url, json=payload, headers=headers)

if response.ok:
    print("Dataset appended successfully.")
else:
    print("Error appending dataset:", response.text)


# In[36]:


get_ipython().system('openai api fine_tunes.append -t "new-questions_prepared.jsonl" -m ada')


# In[ ]:




