FROM tomcat:latest

# Copia el archivo WAR
COPY sql-demo.war /usr/local/tomcat/webapps/

# Copia el archivo .env
COPY .env /usr/local/tomcat/webapps/
COPY mysql-connector-j-9.1.0.zip /tmp/

# Instala las herramientas necesarias y el conector JDBC de MySQL
RUN apt-get update
RUN apt-get install -y default-jdk wget unzip 

RUN unzip /tmp/mysql-connector-j-9.1.0.zip -d /tmp/
RUN mv /tmp/mysql-connector-j-9.1.0/mysql-connector-j-9.1.0.jar /usr/local/tomcat/lib/ 
RUN rm -rf /tmp/mysql-connector-j-9.1.0* /tmp/mysql-connector-j-9.1.0.zip

# Define las variables de entorno
ENV JDBC_URL jdbc:mysql://mysql:3306/example_db
ENV JDBC_USER root
ENV JDBC_PASS root
ENV TABLE_NAME example_table

EXPOSE 8080
