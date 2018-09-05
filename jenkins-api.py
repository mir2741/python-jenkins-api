# coding: utf-8

import jenkins

server = jenkins.Jenkins('http://10.63.17.12:8090/', username='admin', password='admin')
user = server.get_whoami()

#查看Jenkins版本
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

#列出已经创建的job名
jobs = server.get_all_jobs()
for job in jobs:
    print(job['name'])

#创建基本的job
#server.create_job('myjob2',jenkins.EMPTY_CONFIG_XML)
print (server.get_job_config("myjob2"))


#xml模板创建job,
config_xml="""
<project>
  <actions/>
  <description/>
  <keepDependencies>false</keepDependencies>
  <properties>
    <hudson.model.ParametersDefinitionProperty>
      <parameterDefinitions>
        <hudson.model.StringParameterDefinition>
          <name>appname</name>
          <description/>
          <defaultValue/>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>version</name>
          <description/>
          <defaultValue/>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
      </parameterDefinitions>
    </hudson.model.ParametersDefinitionProperty>
  </properties>
  <scm class="hudson.scm.NullSCM"/>
  <canRoam>true</canRoam>
  <disabled>false</disabled>
  <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
  <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
  <triggers/>
  <concurrentBuild>false</concurrentBuild>
  <builders>
    <hudson.tasks.Shell>
      <command>cd /opt/tomcat8 
#docker build -t "127.0.0.1/myproject/centos7/${appname}:${version}" .
#docker push 127.0.0.1/myproject/centos7/${appname}:${version}
sleep 60</command>
    </hudson.tasks.Shell>
  </builders>
  <publishers/>
  <buildWrappers/>
  </project>
"""

server.create_job('myjob3',config_xml)
print (server.get_job_config("myjob3"))