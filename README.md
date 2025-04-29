# Python Email Reader

### Introduction
This Python Email Reader tool is console based application. It reads email from Inbox of an email id.
This tools is basically collect the email ids who are registered into your system, and then you sent the automted confirmation email to them.
You can tweak the code as per your requirements.
- It checks the duplicate ```TO``` email.
- It consider those emails only which are coming from specific email id ```SOURCE_EMAIL```.

### IMPORTANT Configuration
You can find the configuration in ```core/config.py``` file.

### Database Migration
There is table named ```email_store``` is expected to create before executing the application.
So execute below mentioned command before executing the main application, so that the table will be created automatically in the database.

```python init_db.py```

### Application Execution
You can run this application from command line: 

```python main.py```

### Dependency - Libraries
The below mentioned libraries are present in ```requirements.txt``` file.

`imap_tools`
`sqlalchemy`
`mysqlclient`
