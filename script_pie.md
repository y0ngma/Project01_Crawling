## 스크립트

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>리스트</title>  
    <link  rel="stylesheet" href="/static/css/bootstrap.min.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/c3/0.4.11/c3.min.css"/>
    <link href="/css/normalize-e465cb86.css" media="screen" rel="stylesheet" type="text/css" />
    <link href="/css/foundation.min-978d4ce8.css" media="screen" rel="stylesheet" type="text/css" />
    <link href="/css/tomorrow-d7cf0921.css" media="screen" rel="stylesheet" type="text/css" />
    <link href="/css/c3-eb4b9be8.css" media="screen" rel="stylesheet" type="text/css" />
    <link href="/css/style-99fb8989.css" media="screen" rel="stylesheet" type="text/css" />
    <link href="/css/samples/chart_donut-da39a3ee.css" media="screen" rel="stylesheet" type="text/css" />
    <!-- include libraries(jQuery, bootstrap) -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/c3/0.7.3/c3.min.css" rel="stylesheet" />
    <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
    <script src = "https://cdnjs.cloudflare.com/ajax/libs/d3/5.9.7/d3.min.js"></script>
    <script src = "https://cdnjs.cloudflare.com/ajax/libs/c3/0.7.3/c3.min.js"></script>
</head>

<body>
{% include './menu.html' %}
<div class='container'>
    <div class="row">
        <div class="col-md-12">
            <h1> 연간 검색어 집계 </h1>
            <hr />
        </div>
    </div>

    <div class="row">
        <div class="col-md-6">
            <div class="form-inline row justify-content-end" style="margin-top:5px; margin-bottom: 5px;">
                <table class = 'table table-hover'>
                </table>
            </div> 
        </div>
        <div class="col-md-6">
            <!-- 스크립트 넣을 위치 설정 -->
            <div id='chart'></div>
        </div>
    </div>
  
</div>

<script src="/js/ace/ace.js" type="text/javascript"></script>
<script src="/js/ace/mode-javascript.js" type="text/javascript"></script>
<script src="/js/ace/theme-tomorrow.js" type="text/javascript"></script>
<script>
   
    $(function(){
        var arr2 = []
        var arr1 = []

        var str1_1='{{word1}}'
        str1_1=str1_1.replace(/&#x27;/gi, "'").replace(/&#39;/gi, "'"); //정규식
        var objx1 = eval(str1_1)

        var str2_1='{{rank1}}'
        var objy1 = eval(str2_1)

        arr1.push(objx1)
        arr1.push(objy1)
        arr2.push(arr1)


        var str1_5='{{word5}}'
        str1_5=str1_5.replace(/&#x27;/gi, "'").replace(/&#39;/gi, "'");
        var objx5 = eval(str1_5)
        
        var str2_5='{{rank5}}'
        var objy5 = eval(str2_5)

        arr1=[]
        arr1.push(objx5)
        arr1.push(objy5)
        arr2.push(arr1)
        // arr2 = [[objx1, objy1], ... ,[objx5, objy5]]

        var chart = c3.generate({
            bindto:"#chart",
            data: {
                columns:arr2,
                type : 'donut',
                onclick: function (d, i) { console.log("onclick", d, i); },
                onmouseover: function (d, i) { console.log("onmouseover", d, i); },
                onmouseout: function (d, i) { console.log("onmouseout", d, i); }
            },
            donut: {
                title: "기간별 검색어 top5"
            }
        });
    })

</script>
<script src="/js/samples/chart_donut-fca576b3.js" type="text/javascript"></script>


</body>
</html>
```