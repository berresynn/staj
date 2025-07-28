html_doc="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ilk web sayfam</title>
</head>
<body>
    <h1>
      SYN Restoran
    </h1>
    
<div>  

<h2>
     menü1
  </h2>

<ul>
    <li>yemekler</li>
  </ul>
</div>



<div>  

  <h2>
     menü2
</h2>

  <ul>
    <li>içecekler</li>
  </ul>
</div>


</body>
</html>

"""


from bs4 import BeautifulSoupe

soup=BeautifulSoupe(html_doc, "html.parses")

result=soup.prettify()

print(result)


###bu kod yukarıdaki kodun yanlışlarını düzemler örneğin div içerisine yazılanları bir iç satıra alır