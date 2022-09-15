FROM maven AS BUILD
WORKDIR /app
COPY . /app
COPY ./libraries /root/.m2
RUN cd ./target; ls
RUN mvn clean package -Dmaven.test.skip=true

FROM tomcat:8.0-alpine
RUN rm -rf /usr/local/tomcat/webapps/ROOT
COPY --from=BUILD /app/target/calculator.war /usr/local/tomcat/webapps/ROOT.war
EXPOSE 8080
CMD ["catalina.sh","run"]