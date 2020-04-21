Microsoft Windows [Version 10.0.17763.1039]                                        
(c) 2018 Microsoft Corporation. All rights reserved.                               
                                                                                   
C:\Users\GBKXN>cd "OneDrive - Bayer"/college/                                      
                                                                                   
C:\Users\GBKXN\OneDrive - Bayer\College>cd "05-Tools for Data Analytics"           
                                                                                   
C:\Users\GBKXN\OneDrive - Bayer\College\05-Tools for Data Analytics>dir            
 Volume in drive C is WINDOWS                                                      
 Volume Serial Number is 384D-6D5E                                                 
                                                                                   
 Directory of C:\Users\GBKXN\OneDrive - Bayer\College\05-Tools for Data Analytics  
                                                                                   
18/03/2020  19:43    <DIR>          .                                              
18/03/2020  19:43    <DIR>          ..                                             
11/03/2020  17:33           188,923 ChurnPrediction.csv                            
18/03/2020  20:30             8,601 ChurnPrediction.py                             
11/03/2020  17:43           838,984 Slides_Lecture01.pdf                           
18/03/2020  18:18           296,492 Slides_Lecture02.pdf                           
11/03/2020  17:59            19,368 Tools for Data Analytics.docx                  
               5 File(s)      1,352,368 bytes                                      
               2 Dir(s)  18,917,707,776 bytes free                                 
                                                                                   
C:\Users\GBKXN\OneDrive - Bayer\College\05-Tools for Data Analytics>python ChurnPre​‌​
diction.py                                                                         
Traceback (most recent call last):                                                 
  File "ChurnPrediction.py", line 1, in <module>                                   
    import numpy as np                                                             
  File "C:\Users\GBKXN\AppData\Local\Continuum\anaconda3\lib\site-packages\numpy\__​‌​
init__.py", line 140, in <module>                                                  
    from . import _distributor_init                                                
  File "C:\Users\GBKXN\AppData\Local\Continuum\anaconda3\lib\site-packages\numpy\_d​‌​
istributor_init.py", line 34, in <module>                                          
    from . import _mklinit                                                         
ImportError: DLL load failed: The specified module could not be found.             
                                                                                   
C:\Users\GBKXN\OneDrive - Bayer\College\05-Tools for Data Analytics>python ChurnPre​‌​
diction.py                                                                         
Traceback (most recent call last):                                                 
  File "ChurnPrediction.py", line 1, in <module>                                   
    import numpy as np                                                             
  File "C:\Users\GBKXN\AppData\Local\Continuum\anaconda3\lib\site-packages\numpy\__​‌​
init__.py", line 140, in <module>                                                  
    from . import _distributor_init                                                
  File "C:\Users\GBKXN\AppData\Local\Continuum\anaconda3\lib\site-packages\numpy\_d​‌​
istributor_init.py", line 34, in <module>                                          
    from . import _mklinit                                                         
ImportError: DLL load failed: The specified module could not be found.             
                                                                                   
C:\Users\GBKXN\OneDrive - Bayer\College\05-Tools for Data Analytics>python ChurnPre​‌​
diction.py                                                                         
Traceback (most recent call last):                                                 
  File "ChurnPrediction.py", line 1, in <module>                                   
    import numpy as np                                                             
  File "C:\Users\GBKXN\AppData\Local\Continuum\anaconda3\lib\site-packages\numpy\__​‌​
init__.py", line 140, in <module>                                                  
    from . import _distributor_init                                                
  File "C:\Users\GBKXN\AppData\Local\Continuum\anaconda3\lib\site-packages\numpy\_d​‌​
istributor_init.py", line 34, in <module>                                          
    from . import _mklinit                                                         
ImportError: DLL load failed: The specified module could not be found.             
                                                                                   
C:\Users\GBKXN\OneDrive - Bayer\College\05-Tools for Data Analytics>pip install num​‌​
py                                                                                 
'pip' is not recognized as an internal or external command,                        
operable program or batch file.                                                    
                                                                                   
C:\Users\GBKXN\OneDrive - Bayer\College\05-Tools for Data Analytics>python pip inst​‌​
all numpy                                                                          
python: can't open file 'pip': [Errno 2] No such file or directory                 
                                                                                   
C:\Users\GBKXN\OneDrive - Bayer\College\05-Tools for Data Analytics>python -m pip i​‌​
nstall numpy                                                                       
WARNING: pip is configured with locations that require TLS/SSL, however the ssl mod​‌​
ule in Python is not available.                                                    
Requirement already satisfied: numpy in c:\users\gbkxn\appdata\local\continuum\anac​‌​
onda3\lib\site-packages (1.16.4)                                                   
                                                                                   
C:\Users\GBKXN\OneDrive - Bayer\College\05-Tools for Data Analytics>python ChurnPre​‌​
diction.py                                                                         
Traceback (most recent call last):                                                 
  File "ChurnPrediction.py", line 1, in <module>                                   
    import numpy as np                                                             
  File "C:\Users\GBKXN\AppData\Local\Continuum\anaconda3\lib\site-packages\numpy\__​‌​
init__.py", line 140, in <module>                                                  
    from . import _distributor_init                                                
  File "C:\Users\GBKXN\AppData\Local\Continuum\anaconda3\lib\site-packages\numpy\_d​‌​
istributor_init.py", line 34, in <module>                                          
    from . import _mklinit                                                         
ImportError: DLL load failed: The specified module could not be found.             
                                                                                   
C:\Users\GBKXN\OneDrive - Bayer\College\05-Tools for Data Analytics>python -m pip i​‌​
nstall imblearn                                                                    
WARNING: pip is configured with locations that require TLS/SSL, however the ssl mod​‌​
ule in Python is not available.                                                    
Collecting imblearn                                                                
  WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=​‌​
None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the​‌​
 SSL module is not available.")': /simple/imblearn/                                
  WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=​‌​
None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the​‌​
 SSL module is not available.")': /simple/imblearn/                                
  WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=​‌​
None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the​‌​
 SSL module is not available.")': /simple/imblearn/                                
  WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=​‌​
None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the​‌​
 SSL module is not available.")': /simple/imblearn/                                
  WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=​‌​
None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the​‌​
 SSL module is not available.")': /simple/imblearn/                                
  Could not fetch URL https://pypi.org/simple/imblearn/: There was a problem confir​‌​
ming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retri​‌​
es exceeded with url: /simple/imblearn/ (Caused by SSLError("Can't connect to HTTPS​‌​
 URL because the SSL module is not available.")) - skipping                        
  ERROR: Could not find a version that satisfies the requirement imblearn (from ver​‌​
sions: none)                                                                       
ERROR: No matching distribution found for imblearn                                 
                                                                                   
C:\Users\GBKXN\OneDrive - Bayer\College\05-Tools for Data Analytics>
Microsoft Windows [Version 10.0.17763.1039]                                        
(c) 2018 Microsoft Corporation. All rights reserved.                               
                                                                                   
C:\Users\GBKXN>
Microsoft Windows [Version 10.0.17763.1039]                                        ​‌​
039]                                   hts reserved.                               
(c) 2018 Microsoft Corporation. All rig                                            ​‌​
hts reserved.                                                                      
                                       
C:\Users\GBKXN>cd "OneDrive - Bayer"   
                                       
C:\Users\GBKXN\OneDrive - Bayer>dir    
 Volume in drive C is WINDOWS          
 Volume Serial Number is 384D-6D5E     
                                       
 Directory of C:\Users\GBKXN\OneDrive -​‌​
 Bayer                                 
                                       
23/03/2020  09:00    <DIR>          .  
23/03/2020  09:00    <DIR>          .. 
30/07/2018  16:56            26,102 02 
Migration Planning Details.xlsx        
15/11/2018  10:48            13,791 201​‌​
8-09 - Vodafone Billing Issue users.xls​‌​
x                                      
04/09/2018  11:06            11,534 201​‌​
8-09-03-Vodafone Mobile Numbers.xlsx   
11/01/2019  11:40            11,924 201​‌​
8-12-Mobile List.xlsx                  
15/02/2019  14:55            11,146 201​‌​
9-02-12-Acrobat for content factory use​‌​
rs.xlsx                                
28/03/2019  09:43            14,915 201​‌​
9-03-27-Vodafone Connections.xlsx      
23/05/2019  10:48            82,668 201​‌​
9-05-23-Gpupdate.JPG                   
10/06/2019  15:13            10,708 201​‌​
9-06-Mobiles.xlsx                      
23/03/2020  08:40            87,054 202​‌​
0-03-23 Town hall IT.pptx              
10/01/2019  13:13            57,673 Acc​‌​
ess Training Form Readers+WF Roles.docx​‌​
09/10/2019  12:36    <DIR>          Arc​‌​
hive                                   
20/09/2019  10:49    <DIR>          Att​‌​
achments                               
20/02/2020  17:06            17,417 Boa​‌​
rdroom Tech quick Reference.xlsx       
21/02/2020  12:22            20,591 Boa​‌​
rdroom Tech quick Reference_v2.xlsx    
13/04/2018  09:54             4,680 boo​‌​
kmark.htm                              
05/03/2020  17:19    <DIR>          C&G​‌​
 Logistics                             
14/09/2018  13:52            82,415 Car​‌​
diology VR Headset - Checklist v2.docx 
28/05/2018  12:17           535,958 Cha​‌​
nges to Shared Folders.pptx            
31/01/2018  16:15         2,065,114 Cis​‌​
co VPN Client Version.xlsx             
19/02/2020  10:01    <DIR>          Cod​‌​
e                                      
11/03/2020  17:33    <DIR>          Col​‌​
lege                                   
18/03/2020  12:45            17,948 COV​‌​
ID-19-Hardware tracker.xlsx            
21/02/2020  14:29    <DIR>          Dem​‌​
o                                      
06/03/2020  11:57    <DIR>          Des​‌​
ktop                                   
02/05/2018  13:50            12,403 Doc​‌​
ument 2018-01-31T16_18_52.docx         
20/03/2020  17:28    <DIR>          Ema​‌​
il attachments from Flow               
09/10/2019  12:16    <DIR>          eWP​‌​
06/03/2020  15:52    <DIR>          exp​‌​
enses                                  
02/03/2020  15:59    <DIR>          Fav​‌​
orites                                 
13/03/2018  11:29           113,120 Gol​‌​
dDisk Windows 10.xlsx                  
20/09/2019  10:50    <DIR>          HR 
23/03/2020  09:00            22,578 IE-​‌​
R&R-Numbers.xlsx                       
13/02/2020  12:45           120,268 ipa​‌​
d pro test.docx                        
05/02/2020  18:22               270 IQV​‌​
IA Dashboard                           
26/09/2019  15:48            34,304 jun​‌​
k.xls                                  
12/09/2019  12:30           299,533 Lun​‌​
ch 2019-09-12 01_30_00 PM.pdf          
26/07/2019  13:15            42,673 Map​‌​
ping a network drive in Win10.docx     
26/07/2019  13:13           121,309 Map​‌​
ping a network Drive in Win10.pdf      
06/04/2018  11:19           517,051 Map​‌​
ping a network drive.pdf               
09/10/2019  11:40    <DIR>          Mic​‌​
rosoft Teams Chat Files                
09/02/2018  10:18                 0 Mig​‌​
rationToOneDrive.@                     
12/02/2020  18:08                 0 Mig​‌​
rationToOneDrive2.@                    
02/03/2020  15:59    <DIR>          Mus​‌​
ic                                     
20/09/2019  10:49    <DIR>          Not​‌​
ebooks                                 
02/07/2019  16:28            12,773 one​‌​
DriveDemo.docx                         
14/09/2018  13:39            81,829 Oph​‌​
thalmology VR Headset - Checklist v2.do​‌​
cx                                     
14/09/2018  13:36            13,722 Oph​‌​
thalmology VR Headset - Checklist.docx 
18/03/2020  19:35    <DIR>          Per​‌​
sonal                                  
22/03/2020  17:04    <DIR>          Per​‌​
sonal Data                             
23/03/2020  10:53    <DIR>          Pic​‌​
tures                                  
30/07/2018  10:45         2,093,045 Pre​‌​
sentation Support 2018070 EN.pptx      
24/01/2020  15:44    <DIR>          Sha​‌​
ring                                   
04/11/2019  16:33           874,239 Tab​‌​
leau Dashboard for CH 2019-11-04 04_32_​‌​
51 PM.pdf                              
31/10/2019  09:53            18,570 Tho​‌​
mas - Nov19- Car Park Attendance.xlsx  
02/01/2020  10:38               180 Tho​‌​
mas @ Bayer.url                        
02/01/2020  10:37               180 Tho​‌​
mas @ Dublin Business School (DBS).url 
02/12/2019  09:57            38,912 Tho​‌​
mas Higgins Dec19 Car Park Attendance.x​‌​
ls                                     
20/12/2019  15:03            56,085 Tim​‌​
esheet 2019.xlsx                       
19/03/2020  16:57            56,181 Tim​‌​
esheet 2020.xlsx                       
09/10/2019  11:19    <DIR>          toR​‌​
ead                                    
15/03/2018  15:38         1,300,929 UK-​‌​
IE - regional_workshop_country_profile_​‌​
emea.potx                              
09/10/2019  12:35    <DIR>          uns​‌​
orted                                  
20/09/2019  10:49    <DIR>          Use​‌​
rSyncSettings                          
09/10/2019  12:20    <DIR>          Vee​‌​
va                                     
02/03/2020  15:59    <DIR>          Vid​‌​
eos                                    
24/01/2019  17:46           112,075 Vod​‌​
afone account overview.JPG             
              42 File(s)      9,013,867​‌​
 bytes                                 
              26 Dir(s)  18,981,838,848​‌​
 bytes free                            
                                       
C:\Users\GBKXN\OneDrive - Bayer>cd code​‌​
/github                                
                                       
C:\Users\GBKXN\OneDrive - Bayer\Code\gi​‌​
thub>cd B8IT105                        
                                       
C:\Users\GBKXN\OneDrive - Bayer\Code\gi​‌​
thub\B8IT105>dir                       
 Volume in drive C is WINDOWS          
 Volume Serial Number is 384D-6D5E     
                                       
 Directory of C:\Users\GBKXN\OneDrive -​‌​
 Bayer\Code\github\B8IT105             
                                       
23/03/2020  18:36    <DIR>          .  
23/03/2020  18:36    <DIR>          .. 
23/03/2020  18:36             1,312 imp​‌​
ort_worldometers.py                    
16/03/2020  20:44               115 REA​‌​
DME.md                                 
               2 File(s)          1,427​‌​
 bytes                                 
               2 Dir(s)  18,918,797,312​‌​
 bytes free                            
                                       
C:\Users\GBKXN\OneDrive - Bayer\Code\gi​‌​
thub\B8IT105>python import_worldometers​‌​
.py                                    
Traceback (most recent call last):     
  File "C:\Users\GBKXN\AppData\Local\Co​‌​
ntinuum\anaconda3\lib\site-packages\url​‌​
lib3\connectionpool.py", line 588, in u​‌​
rlopen                                 
    conn = self._get_conn(timeout=pool_​‌​
timeout)                               
  File "C:\Users\GBKXN\AppData\Local\Co​‌​
ntinuum\anaconda3\lib\site-packages\url​‌​
lib3\connectionpool.py", line 248, in _​‌​
get_conn                               
    return conn or self._new_conn()    
  File "C:\Users\GBKXN\AppData\Local\Co​‌​
ntinuum\anaconda3\lib\site-packages\url​‌​
lib3\connectionpool.py", line 816, in _​‌​
new_conn                               
    raise SSLError("Can't connect to HT​‌​
TPS URL because the SSL "              
urllib3.exceptions.SSLError: Can't conn​‌​
ect to HTTPS URL because the SSL module​‌​
 is not available.                     
                                       
During handling of the above exception,​‌​
 another exception occurred:           
                                       
Traceback (most recent call last):     
  File "C:\Users\GBKXN\AppData\Local\Co​‌​
ntinuum\anaconda3\lib\site-packages\req​‌​
uests\adapters.py", line 449, in send  
    timeout=timeout                    
  File "C:\Users\GBKXN\AppData\Local\Co​‌​
ntinuum\anaconda3\lib\site-packages\url​‌​
lib3\connectionpool.py", line 638, in u​‌​
rlopen                                 
    _stacktrace=sys.exc_info()[2])     
  File "C:\Users\GBKXN\AppData\Local\Co​‌​
ntinuum\anaconda3\lib\site-packages\url​‌​
lib3\util\retry.py", line 399, in incre​‌​
ment                                   
    raise MaxRetryError(_pool, url, err​‌​
or or ResponseError(cause))            
urllib3.exceptions.MaxRetryError: HTTPS​‌​
ConnectionPool(host='www.worldometers.i​‌​
nfo', port=443): Max retries exceeded w​‌​
ith url: /coronavirus/ (Caused by SSLEr​‌​
ror("Can't connect to HTTPS URL because​‌​
 the SSL module is not available."))   
                                       
During handling of the above exception,​‌​
 another exception occurred:           
                                       
Traceback (most recent call last):     
  File "import_worldometers.py", line 1​‌​
8, in <module>                         
    response = requests.get('https://ww​‌​
w.worldometers.info/coronavirus/', head​‌​
ers=headers)                           
  File "C:\Users\GBKXN\AppData\Local\Co​‌​
ntinuum\anaconda3\lib\site-packages\req​‌​
uests\api.py", line 75, in get         
    return request('get', url, params=p​‌​
arams, **kwargs)                       
  File "C:\Users\GBKXN\AppData\Local\Co​‌​
ntinuum\anaconda3\lib\site-packages\req​‌​
uests\api.py", line 60, in request     
    return session.request(method=metho​‌​
d, url=url, **kwargs)                  
  File "C:\Users\GBKXN\AppData\Local\Co​‌​
ntinuum\anaconda3\lib\site-packages\req​‌​
uests\sessions.py", line 533, in reques​‌​
t                                      
    resp = self.send(prep, **send_kwarg​‌​
s)                                     
  File "C:\Users\GBKXN\AppData\Local\Co​‌​
ntinuum\anaconda3\lib\site-packages\req​‌​
uests\sessions.py", line 646, in send  
    r = adapter.send(request, **kwargs)​‌​
                                       
  File "C:\Users\GBKXN\AppData\Local\Co​‌​
ntinuum\anaconda3\lib\site-packages\req​‌​
uests\adapters.py", line 514, in send  
    raise SSLError(e, request=request) 
requests.exceptions.SSLError: HTTPSConn​‌​
ectionPool(host='www.worldometers.info'​‌​
, port=443): Max retries exceeded with 
url: /coronavirus/ (Caused by SSLError(​‌​
"Can't connect to HTTPS URL because the​‌​
 SSL module is not available."))       
                                       
C:\Users\GBKXN\OneDrive - Bayer\Code\gi​‌​
thub\B8IT105>python import_worldometers​‌​
.py                                    
Traceback (most recent call last):     
  File "C:\Users\GBKXN\AppData\Local\Co​‌​
ntinuum\anaconda3\lib\site-packages\url​‌​
lib3\connectionpool.py", line 588, in u​‌​
rlopen                                 
    conn = self._get_conn(timeout=pool_​‌​
timeout)                               
  File "C:\Users\GBKXN\AppData\Local\Co​‌​
ntinuum\anaconda3\lib\site-packages\url​‌​
lib3\connectionpool.py", line 248, in _​‌​
get_conn                               
    return conn or self._new_conn()    
  File "C:\Users\GBKXN\AppData\Local\Co​‌​
ntinuum\anaconda3\lib\site-packages\url​‌​
lib3\connectionpool.py", line 816, in _​‌​
new_conn                               
    raise SSLError("Can't connect to HT​‌​
TPS URL because the SSL "              
urllib3.exceptions.SSLError: Can't conn​‌​
ect to HTTPS URL because the SSL module​‌​
 is not available.                     
                                       
During handling of the above exception,​‌​
 another exception occurred:           
                                       
Traceback (most recent call last):     
  File "C:\Users\GBKXN\AppData\Local\Co​‌​
ntinuum\anaconda3\lib\site-packages\req​‌​
uests\adapters.py", line 449, in send  
    timeout=timeout                    
  File "C:\Users\GBKXN\AppData\Local\Co​‌​
ntinuum\anaconda3\lib\site-packages\url​‌​
lib3\connectionpool.py", line 638, in u​‌​
rlopen                                 
    _stacktrace=sys.exc_info()[2])     
  File "C:\Users\GBKXN\AppData\Local\Co​‌​
ntinuum\anaconda3\lib\site-packages\url​‌​
lib3\util\retry.py", line 399, in incre​‌​
ment                                   
    raise MaxRetryError(_pool, url, err​‌​
or or ResponseError(cause))            
urllib3.exceptions.MaxRetryError: HTTPS​‌​
ConnectionPool(host='www.worldometers.i​‌​
nfo', port=443): Max retries exceeded w​‌​
ith url: /coronavirus/ (Caused by SSLEr​‌​
ror("Can't connect to HTTPS URL because​‌​
 the SSL module is not available."))   
                                       
During handling of the above exception,​‌​
 another exception occurred:           
                                       
Traceback (most recent call last):     
  File "import_worldometers.py", line 1​‌​
8, in <module>                         
    response = requests.get('https://ww​‌​
w.worldometers.info/coronavirus/', head​‌​
ers=headers)                           
  File "C:\Users\GBKXN\AppData\Local\Co​‌​
ntinuum\anaconda3\lib\site-packages\req​‌​
uests\api.py", line 75, in get         
    return request('get', url, params=p​‌​
arams, **kwargs)                       
  File "C:\Users\GBKXN\AppData\Local\Co​‌​
ntinuum\anaconda3\lib\site-packages\req​‌​
uests\api.py", line 60, in request     
    return session.request(method=metho​‌​
d, url=url, **kwargs)                  
  File "C:\Users\GBKXN\AppData\Local\Co​‌​
ntinuum\anaconda3\lib\site-packages\req​‌​
uests\sessions.py", line 533, in reques​‌​
t                                      
    resp = self.send(prep, **send_kwarg​‌​
s)                                     
  File "C:\Users\GBKXN\AppData\Local\Co​‌​
ntinuum\anaconda3\lib\site-packages\req​‌​
uests\sessions.py", line 646, in send  
    r = adapter.send(request, **kwargs)​‌​
                                       
  File "C:\Users\GBKXN\AppData\Local\Co​‌​
ntinuum\anaconda3\lib\site-packages\req​‌​
uests\adapters.py", line 514, in send  
    raise SSLError(e, request=request) 
requests.exceptions.SSLError: HTTPSConn​‌​
ectionPool(host='www.worldometers.info'​‌​
, port=443): Max retries exceeded with 
url: /coronavirus/ (Caused by SSLError(​‌​
"Can't connect to HTTPS URL because the​‌​
 SSL module is not available."))       
                                       
C:\Users\GBKXN\OneDrive - Bayer\Code\gi​‌​
thub\B8IT105>