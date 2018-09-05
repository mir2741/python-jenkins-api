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
print server.get_job_config("myjob2")


#xml模板创建job,
config_xml="""
<project>
  <actions/>
  <description></description>
  <keepDependencies>false</keepDependencies>
  <properties>
    <jenkins.model.BuildDiscarderProperty>
      <strategy class="hudson.tasks.LogRotator">
        <daysToKeep>4</daysToKeep>
        <numToKeep>6</numToKeep>
        <artifactDaysToKeep>-1</artifactDaysToKeep>
        <artifactNumToKeep>-1</artifactNumToKeep>
      </strategy>
    </jenkins.model.BuildDiscarderProperty>
  </properties>
  <scm class="hudson.scm.NullSCM"/>
  <canRoam>true</canRoam>
  <disabled>false</disabled>
  <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
  <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
  <triggers/>
  <concurrentBuild>false</concurrentBuild>
  <builders/>
  <publishers/>
  <buildWrappers/>
</project>
"""

server.create_job('myjob3',config_xml)
print server.get_job_config("myjob3")