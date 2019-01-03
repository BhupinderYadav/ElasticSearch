# coding=UTF-8

# creating rest requests to elastic search tool
import requests
import json
import wx
import json
import urllib
import dicttoxml #to convert in xml
import xml.dom.minidom


def search(url, search_item):
    headers = {'Accept': 'application/json', 'Content-type': 'application/json'}
    query = json.dumps({
        "query": {
            "match": {
                "nocrefid": search_item  # field to be search
            }
        }
    })
    # function to make a search in elastic search tool
    response = requests.get(url, data=query, headers=headers)
    results = response.json()
    response.close()
    return results

def formatted_results(results):
    data = [doc for doc in results['hits']['hits']]
    for doc in data:
        print("%s  %s" % (doc['_id'], doc['_source']['nocrefid']))
        print("%s " % ( doc['_source']['prod']))
        print("%s " % ( doc['_source']['message']))

# post method for elastic search

def post_doc(url, doc_data={}):
    headers = {'Accept': 'application/json', 'Content-type': 'application/json'}
    query = json.dumps(doc_data)
    response = requests.post(url, data=query)
    print(response)

if __name__ == '__main__':
    url_search = 'http://localhost:9200/w6tasks/logs/_search'
    url_create = 'http://localhost:9200/w6tasks/logs/'
    results = search(url_search, "MU_Test_5")
    formatted_results(results)
    output_xml = dicttoxml.dicttoxml(results)
    output_xml_file =  open("ElasticSearch_Results.txt", "w")
    output_xml_file.write(output_xml)
    output_xml_file.close()

