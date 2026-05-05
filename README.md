<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
     .hero-banner{
        background-color: lch(69.37% 29.19 197.13);
        height: 200px;
        width: 95vw;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        font-family:Arial, Helvetica, sans-serif;
     }
     .hero-title{
        font-size: 2rem;
        font-weight: bold;
        line-height: 3rem;
     }
     .hero-sub{
        line-height: 1.5rem;
     }
     .badge-row{
        margin-top: 1rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        /* line-height: 3.5rem; */
        width: 90vw;
     }
     .gh-badge{
        display: flex;
        justify-content:space-between;
        align-items: center;
        /* background-color: blueviolet; */
        font-size: .8rem;
        height: 1rem;
        /* width: 10rem; */
        line-height: 1.5rem;
        color: antiquewhite;
     }
     .bl{
        background-color: rgb(37, 37, 37);
        border-top-left-radius: 5px;
        border-bottom-left-radius: 5px;
        width: 4rem;
        padding-left: .5rem;
        /* padding-right: .5rem;  */
     }
     .br{
        border-top-right-radius: 5px;
        border-bottom-right-radius: 5px;
        padding-left: .5rem;
        padding-right: .5rem;
     }
     .green{  background-color: green;}
     .blue{  background-color: blue;}
     .teal{  background-color: teal;}
     .orange{  background-color: orange;}
     .purple{  background-color: purple;}
     .red{  background-color: red;}
    </style>
</head>
<body>
    <div class="hero-banner">
        <div class="hero-title">🌿 Crop and Weed Detection System</div>
        <div class="hero-sub">
          Two-stage YOLOv8 pipeline for precision agriculture in Indian soybean fields<br>
          <em>Final Year B.E. Project · Neotech Campus, Vadodara · GTU · 2025</em>
        </div>
        <div class="badge-row">
          <div class="gh-badge"><span class="bl">accuracy</span><span class="br green">90%+</span></div>
          <div class="gh-badge"><span class="bl">framework</span><span class="br blue">YOLOv8</span></div>
          <div class="gh-badge"><span class="bl">dataset</span><span class="br teal">MH-16</span></div>
          <div class="gh-badge"><span class="bl">species</span><span class="br orange">16 </span></div>
          <div class="gh-badge"><span class="bl">python</span><span class="br purple">3.10</span></div>
          <div class="gh-badge"><span class="bl">license</span><span class="br red">MIT</span></div>
        </div>
    </div>
</body>
</html>
