#old implementation
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailDict = {}
        for email in emails:
            localName,domainName = email.split("@")
            localName = localName.split("+")[0]
            localName = localName.replace(".","")
            emailDict.update({localName +"@" + domainName:1})
            
        return len(emailDict)