#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

contents = ''

data = requests.get('https://ndc-api-beta.arukascloud.io/ndc9.json').json()

for (key, value) in data.items():
    if key != '':
        print(key)
        contents += (
                """
        <ns1:DictionaryEntry>
            <ns1:InputString>%s</ns1:InputString>
            <ns1:OutputString>%s</ns1:OutputString>
            <ns1:PartOfSpeech>noun</ns1:PartOfSpeech>
            <ns1:CommentData1>[NDC9] %s</ns1:CommentData1>
            <ns1:URL>https://ndc-api-beta.arukascloud.io/ndc9/%s</ns1:URL>
            <ns1:Priority>150</ns1:Priority>
            <ns1:ReverseConversion>true</ns1:ReverseConversion>
            <ns1:CommonWord>false</ns1:CommonWord>
        </ns1:DictionaryEntry>
                """ % (key, key + ' ' + value['label@ja'], "\n".join(value['note@ja']) if value['note@ja'] else '', key)
        )

with open('ndc9.dctx', 'wt', encoding='utf-8') as f:
    f.write("""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<ns1:Dictionary xmlns:ns1="http://www.microsoft.com/ime/dctx" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<ns1:DictionaryHeader>
		<ns1:DictionaryGUID>{80FD60C4-8453-498F-9DD9-3F2B9F622D23}</ns1:DictionaryGUID>
		<ns1:DictionaryLanguage>ja-jp</ns1:DictionaryLanguage>
		<ns1:DictionaryVersion>1</ns1:DictionaryVersion>
		<ns1:SourceURL>https://ndc.dev/</ns1:SourceURL>
		<ns1:CommentInsertion>true</ns1:CommentInsertion>
		<ns1:DictionaryInfo Language="ja-jp">
			<ns1:ShortName>NDC辞書(9)</ns1:ShortName>
			<ns1:LongName>日本十進分類法辞書(9版)</ns1:LongName>
			<ns1:Description>この辞書には、日本十進分類法が含まれています。</ns1:Description>
			<ns1:Copyright>CC-BY JLA / Converted by Ryuuji Yoshimoto</ns1:Copyright>
			<ns1:CommentHeader1></ns1:CommentHeader1>
		</ns1:DictionaryInfo>
	</ns1:DictionaryHeader>
	%s
</ns1:Dictionary>""" % contents)
