# -*- coding: utf-8 -*-

import unittest
from collections import namedtuple

from api import counts_pages_words



class MockRequestsNewYorkTimes(object):
	def __getattr__(self, name):
		#from nose.tools import set_trace; set_trace() 
		if name == 'url':
			UrlMock = namedtuple('url', ['title'])
			return UrlMock(title='article')
		else:
			return NYTIMES_GARBAGE

class TestCountsPagesWords(unittest.TestCase):

	def test_counts_pages_words(self):
		def mock_requests_get(url):
			return MockRequestsNewYorkTimes()
		import requests
		old_requests_get = requests.get
		requests.get = mock_requests_get
		URL1 = "http://www.nytimes.com"
		results = counts_pages_words(URL1)
		found_words = [(u'Cadillac',3), (u'Hummer',2), (u'BAM',2)]
		for fw in found_words:
			self.assertIn(fw, results['freq_dist'])
		requests.get = old_requests_get

NYTIMES_GARBAGE = """<!DOCTYPE html>
<!--[if IE]><![endif]-->
<html lang="en" class="NYT5Style">
<head>
<title>The New York Times - Breaking News, World News &amp; Multimedia</title>
<meta http-equiv="X-UA-Compatible" content="IE=edge" /> 
<meta name="robots" content="noarchive,noodp,noydir">
<meta name="description" content="Find breaking news, multimedia, reviews &amp; opinion on Washington, business, sports, movies, travel, books, jobs, education, real estate, cars &amp; more at nytimes.com.">
<meta name="keywords" content="Congressional Budget Office,Patient Protection and Affordable Care Act (2010),Farm Bill (US),Snowden, Edward J,Rogers, Michael J (1963- ),House Committee on the Judiciary,Republican Party,Comey, James B,House Committee on Intelligence,Cole, James M,National Security Agency,Classified Information and State Secrets,News and News Media,United States Politics and Government,Surveillance of Citizens by Government,Goodlatte, Robert W,West Village (Manhattan, NY),Heroin,Police Department (NYC),Hoffman, Philip Seymour,de Blasio, Bill,St Patrick's Day,Bloomberg, Michael R,Giuliani, Rudolph W,Fifth Avenue (Manhattan, NY),Parades,Homosexuality,Dinkins, David N,Education (K-12),Computers and the Internet,ConnectED,Obama, Barack,United States Army,Art,Graffiti,Espionage and Intelligence Services,National Security Agency,Berlin (Germany),Teufelsberg,Cold War Era,Letters,Stanislaw Dziwisz,Roman Catholic Church,John Paul II,Books and Literature,Poland,South China Sea,Philippines,Czechoslovakia,World War II (1939-45),Aquino, Benigno S III,China,Community Colleges,Colleges and Universities,Tennessee,Tuition,Haslam, Bill,Gates, Bill,Nadella, Satya,Microsoft Corporation,Executives and Management (Theory),Ski Jumping,Olympic Games (2014),Japan,Bouley, David,TriBeCa (Manhattan, NY),Bouley Botanical,Agriculture and Farming">
<meta name="CG" content="Homepage">
<meta name="SCG" content="">
<meta name="PT" content="Homepage">
<meta name="PST" content="">
<meta name="HOMEPAGE_TEMPLATE_VERSION" content="300">
<meta name="application-name" content="The New York Times" />
<meta name="msapplication-starturl" content="http://www.nytimes.com/" />
<meta name="msapplication-task" content="name=Search;action-uri=http://query.nytimes.com/search/sitesearch?src=iepin;icon-uri=http://css.nyt.com/images/icons/search.ico" />
<meta name="msapplication-task" content="name=Most Popular;action-uri=http://www.nytimes.com/gst/mostpopular.html?src=iepin;icon-uri=http://css.nyt.com/images/icons/mostpopular.ico" />
<meta name="msapplication-task" content="name=Video;action-uri=http://video.nytimes.com/?src=iepin;icon-uri=http://css.nyt.com/images/icons/video.ico" />
<meta name="msapplication-task" content="name=Homepage;action-uri=http://www.nytimes.com?src=iepin&amp;adxnnl=1;icon-uri=http://css.nyt.com/images/icons/homepage.ico" />
<link rel="shortcut icon" href="http://css.nyt.com/images/icons/nyt.ico" />
<link rel="alternate" type="application/rss+xml" title="RSS" href="http://www.nytimes.com/services/xml/rss/nyt/HomePage.xml">
<link rel="alternate" media="handheld" href="http://mobile.nytimes.com">    
<link rel="stylesheet" type="text/css" href="http://css.nyt.com/css/0.1/screen/build/homepage/styles.css">
<link rel="stylesheet" type="text/css" media="print" href="http://css.nyt.com/css/0.1/print/styles.css">
<!--[if IE]>
    <link rel="stylesheet" type="text/css" href="http://css.nyt.com/css/0.1/screen/build/homepage/ie.css?v=012611">
<![endif]-->
<!--[if IE 6]>
    <link rel="stylesheet" type="text/css" href="http://css.nyt.com/css/0.1/screen/build/homepage/ie6.css">
<![endif]-->
<!--[if lt IE 9]>
	<script src="http://js.nyt.com/js/html5shiv.js"></script>
<![endif]-->
<script type="text/javascript" src="http://js.nyt.com/js2/build/sitewide/sitewide.js"></script>
<script type="text/javascript" src="http://js.nyt.com/js2/build/homepage/top.js"></script>
<script src="//typeface.nytimes.com/miq8eej.js"></script>
<script>try{Typekit.load();}catch(e){}</script>
<!-- ADXINFO classification="blank-but-count-imps" campaign="KRUX_DIGITAL_CONTROL_SCRIPT_LIVE_HP" priority="9100" isInlineSafe="N" width="1" height="1" --><!-- BEGIN Krux Controltag -->
<script class="kxct" data-id="HrUwtkcl" data-version="async:1.7" type="text/javascript">
  window.Krux||((Krux=function(){Krux.q.push(arguments)}).q=[]);
  (function(){
    var k=document.createElement('script');k.type='text/javascript';k.async=true;var m,src=(m=location.href.match(/\bkxsrc=([^&]+)\b/))&&decodeURIComponent(m[1]);
    k.src=src||(location.protocol==='https:'?'https:':'http:')+'//cdn.krxd.net/controltag?confid=HrUwtkcl';
    var s=document.getElementsByTagName('script')[0];s.parentNode.insertBefore(k,s);
  })();
</script>
<!-- END Krux Controltag -->
</head>
<body id="home">
<a name="top"></a>
<div id="shell">

<!-- ADXINFO classification="Text_Link" campaign="nyt2014_abTest_bar1_janhd_cookdpr" priority="9200" isInlineSafe="N" width="0" height="0" --><script>
  document.cookie='bar1janhd=bau;domain=.nytimes.com;path=/';
</script>

<ul id="memberTools">

<!-- ADXINFO classification="Share_of_Voice_Tile_-_Left" campaign="nyt2014_bar1_digihd_nyt5bau_hpsf_3LWW7_3LWW8_3LWW9" priority="9000" isInlineSafe="Y" width="184" height="90" --><span class="ts-20140128-1133"></span>
<style type="text/css">
.NYT5Style .masthead-tools #duallink {
    display: inline;
    vertical-align: top;
}
#duallink {
  border:none;
}
#duallink > a {
    -moz-box-sizing: border-box;
    background-color: #6288A5;
    border: 1px solid #4D7B9F;
    border-radius: 3px;
    color: #FFFFFF;
    display: inline-block;
    font-size: 1em;
    font-weight: bold;
    font-family: nyt-franklin,nyt-franklin-1,'Helvetica Neue',Arial,sans-serif;
    padding: 7px 10px 6px;
    text-transform: uppercase;
    text-decoration: none;
}
#duallink > a:hover {
    background-color: #326891;
    border: 1px solid #265E8B;
    text-decoration: none;
}
#hovercard {
    width: 450px;
    height: 330px;
    display: none;
    z-index: 99999999;
    background-color: #fff;
    border: 1px solid #ccc;
    position: absolute;
    left: -290px;
    top: 29px;

    -moz-box-shadow: 0 0 5px #888;
    -webkit-box-shadow: 0 0 5px#888;
    box-shadow: 0 0 5px #888;

    text-align: left;
}
#hovercard:before {
    content: url(http://graphics8.nytimes.com/marketing/bar1jsimages/arrowup.png);
    position: absolute;
    left: 342px;
    top: -9px;
    width: 25px;
    height: 18px;
    display:block;
}
h3.hover-title {
    font-style: normal;
    font-size: 16px;
    font-weight: 700;
    line-height: 20px;
    font-family: nyt-franklin,nyt-franklin-1,'Helvetica Neue',Arial,sans-serif;
    color: #000;
    width: 190px;
    white-space: normal;
}
.split-dig {
    width: 224px;
    border-right: 1px solid #F1F1F1;
    margin: 0;
    padding: 0;
    min-height: 330px;
    background: #fff url('http://graphics8.nytimes.com/adx/images/ADS/36/05/ad.360598/devices_tri_201401_v2.png') center 34px no-repeat;
    float: left;
    position: relative;
}
.split-dig-content {
    padding: 145px 0 0 17px;
}
.split-ada {
    width: 225px;
    margin: 0;
    padding: 0;
    min-height: 330px;
    background: #fff url('http://graphics8.nytimes.com/adx/images/ADS/36/05/ad.360598/devices_paper_201401_v2.png') center 34px no-repeat;
    float: right;
    position: relative;
}
.split-ada-content {
    padding: 145px 0 0 15px;
}
.split-dig:hover, 
.split-ada:hover {
  background-color: #F2F6F9;
}
.hover-subhead {
    font-family: nyt-franklin, nyt-franklin-1, 'Helvetica Neue', Arial;
    font-weight: 500;
    font-size: 13px;
    line-height: 18px;
    color: #333;
    margin-top: 14px;
    width: 185px;
    white-space: normal;
}
.split-ada-content .hover-subhead {
    width: 200px;
}
a.nyt-button-actions {
    background: #F7F7F5;
    color: #6E6E6C;
    width: 188px;
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    border-radius: 3px;  
    border: 1px solid #ccc !important;
    text-transform: uppercase;
    font: 11px nyt-franklin, nyt-franklin-1, "Helvetica Neue", Arial, sans-serif;
    text-align: center;
    padding: 6px 0;
    cursor: pointer;
    display: block;
    position: absolute;
    bottom:15px;
}
a.nyt-button-actions:hover {
    background: #3C6791; 
    color: #fff !important;
    text-decoration: none !important;
}
a.nyt-button-actions.highlightButton:link,
a.nyt-button-actions.highlightButton:visited {
        color: #fff;
        background: #3C6791; 
        text-decoration: none !important;
}
</style>


<li id="duallink" class="user-subscriptions-menu user-subscriptions-group"><a id="nyt-button-sub" class="" href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=Bar1&sn2=5b35bc29/49f095e7&sn1=64aeb60a/889a8ad3&camp=nyt2014_bar1_digihd_nyt5bau_hpsf_3LWW7_3LWW8_3LWW9&ad=bar1hover_nyt5_bau_hpsf_3LWW9_3LWW7_3LWW8&goto=http%3A%2F%2Fwww%2Enytimes%2Ecom%2Fsubscriptions%2FMultiproduct%2Flp3004%2Ehtml%3Fadxc%3D234206%26adxa%3D360598%26page%3Dhomepage.nytimes.com/index.html%26pos%3DBar1%26campaignId%3D3LWW9" target="_blank">Subscribe Now</a>

    <div id="hovercard">
        <div class="split split-dig">
            <div class="split-dig-content">
                <h3 class="hover-title">
                          Try a Digital Subscription Today for Just
                          99&cent; for Your First 4 Weeks
                        </h3>
                        <p class="hover-subhead" style="margin-top:6px">Get unlimited access to NYTimes.com and NYTimes apps.
                        </p>
                <a class="nyt-button-actions" href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=Bar1&sn2=5b35bc29/49f095e7&sn1=64aeb60a/889a8ad3&camp=nyt2014_bar1_digihd_nyt5bau_hpsf_3LWW7_3LWW8_3LWW9&ad=bar1hover_nyt5_bau_hpsf_3LWW9_3LWW7_3LWW8&goto=http%3A%2F%2Fwww%2Enytimes%2Ecom%2Fsubscriptions%2FMultiproduct%2Flp5558%2Ehtml%3Fadxc%3D234206%26adxa%3D360598%26page%3Dhomepage.nytimes.com/index.html%26pos%3DBar1%26campaignId%3D3LWW7" target="_blank">Get Digital</a>
            </div>
        </div>
        <div class="split-ada">
            <div class="split split-ada-content">
                <h3 class="hover-title">
                  Get 50% Off 12 Weeks of Home Delivery and Free All Digital Access
                </h3>
                <p class="hover-subhead" style="margin-top:6px">
                    All print options include free, unlimited access to NYTimes.com and NYTimes apps.
                </p>
                <a class="nyt-button-actions" target="_blank" href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=Bar1&sn2=5b35bc29/49f095e7&sn1=28b4d37a/7d304080&camp=nyt2014_bar1_digihd_nyt5bau_hpsf_3LWW7_3LWW8_3LWW9&ad=bar1hover_nyt5_bau_hpsf_3LWW9_3LWW7_3LWW8&goto=https%3A%2F%2Fnytimesathome%2Ecom%2Fhd%2F205%3FMediaCode%3DWB7AA%26CMP%3D3LWW8">
                    Get Home Delivery
                </a>
            </div>
        </div>
    </div>
</li>




<script type="text/javascript">
(function ($, global) {
    "use strict";

    $('#duallink').mouseenter(function(){
        $('#hovercard', this).fadeIn('fast');
    });
    $('#duallink').mouseleave(function(){
        $('#hovercard', this).fadeOut('fast');
    });

})(window.NYTD && window.NYTD.jQuery || window.jQuery, window);
</script>


                <li><a href="/auth/login?URI=http://">Log In</a></li> 
        <li><a href="/gst/regi.html" onClick="dcsMultiTrack('WT.z_ract', 'Regnow', 'WT.z_rprod', 'Masthead','WT.z_dcsm','1');">Register Now</a></li>
            

</ul>
<div class="mainTabsContainer tabsContainer">
<ul id="mainTabs" class="mainTabs tabs">
<li  class="first"><a href="http://www.nytimes.com/pages/todayspaper/index.html">Today's Paper</a></li>
<li><a href="http://video.nytimes.com/">Video</a></li>
<li><a href="http://www.nytimes.com/mostpopular">Most Popular</a></li>
</ul>
</div><!--close .tabsContainer -->
<div id="editionToggle" class="editionToggle">
Edition: <span id="editionToggleUS"><a href="http://www.nytimes.com" onmousedown="dcsMultiTrack('DCS.dcssip','www.nytimes.com','DCS.dcsuri','/toggleIHTtoNYT.html','WT.ti','toggleIHTtoNYT','WT.z_dcsm','1');" onclick="NYTD.EditionPref.setUS();">U.S.</a></span> / <span id="editionToggleGlobal"><a href="http://global.nytimes.com" onmousedown="dcsMultiTrack('DCS.dcssip','www.nytimes.com','DCS.dcsuri','/toggleNYTtoIHT.html','WT.ti','toggleNYTtoIHT','WT.z_dcsm','1');" onclick="NYTD.EditionPref.setGlobal();">Global</a></span>
</div><!--close editionToggle -->
<div id="page" class="tabContent active">
<div id="masthead">

<div class="singleAd" id="TopLeft">
<!-- ADXINFO classification="Share_of_Voice_Tile_-_Left" campaign="Marc_Jacobs_1917519_2014-nyt8" priority="8500" isInlineSafe="N" width="184" height="90" --><a href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=TopLeft&sn2=ab8a95f5/87622a3f&sn1=64816686/f2c0e1fa&camp=Marc_Jacobs_1917519_2014-nyt8&ad=Marc_Jacobs_Left_RetroFrames_Jan-Feb2014&goto=http%3A%2F%2Fwww%2Emarcjacobs%2Ecom%2Fmarc%2Dby%2Dmarc%2Djacobs%2Feyewear%2Fmmj389%2Fmarc%2Dby%2Dmarc%2Djacobs%2Dretro%2Dframe%3Fsort%3D%26utm%5Fsource%3Dnyt14%26utm%5Fmedium%3Dlefttile%26utm%5Fcampaign%3Dretroframe" target="_blank">
<img src="http://graphics8.nytimes.com/adx/images/ADS/36/28/ad.362832/NYT_RETROFRAMES_LEFT.jpg" width="184" height="90" border="0"></a>
</div>


<div class="singleAd" id="TopRight">
<!-- ADXINFO classification="Share_of_Voice_Tile_-_Right" campaign="Marc_Jacobs_1917519_2014-nyt8" priority="8500" isInlineSafe="N" width="184" height="90" --><a href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=TopRight&sn2=361d9a2f/d5c54928&sn1=8ffd4833/9a0eebfb&camp=Marc_Jacobs_1917519_2014-nyt8&ad=Marc_Jacobs_Right_RetroFrames_Jan-Feb2014&goto=http%3A%2F%2Fwww%2Emarcjacobs%2Ecom%2Fmarc%2Dby%2Dmarc%2Djacobs%2Feyewear%2Fmmj389%2Fmarc%2Dby%2Dmarc%2Djacobs%2Dretro%2Dframe%3Fsort%3D%26utm%5Fsource%3Dnyt14%26utm%5Fmedium%3Drighttile%26utm%5Fcampaign%3Dretroframe" target="_blank">
<img src="http://graphics8.nytimes.com/adx/images/ADS/36/28/ad.362833/NYT_RETROFRAMES_RIGHT.jpg" width="184" height="90" border="0"></a>
</div>


<script type="text/javascript">
              if (/iPad|iPod|iPhone/.test(navigator.userAgent)){
                document.write('<img id="mastheadLogo" width="379" height="64" alt="The New York Times" src="http://i1.nyt.com/svg/nytlogo_379x64.svg">');
              } else {
                document.write('<img id="mastheadLogo" width="379" height="64" alt="The New York Times" src="http://i1.nyt.com/images/misc/nytlogo379x64.gif">');
              }
            </script>
<noscript>
<img id="mastheadLogo" width="379" height="64" alt="The New York Times" src="http://i1.nyt.com/images/misc/nytlogo379x64.gif"/>
</noscript>

<div id="date"><p>Tuesday, February 4, 2014 <span id="lastUpdate">Last Update: </span><span class="timestamp">11:35 PM ET</span></p></div>
</div><!--end #masthead -->

<div id="toolbar">


<div id="toolbarSearchContainer">

<div id="toolbarSearch">
<div class="inlineSearchControl">
<form id="searchForm" name="searchForm" method="get" action="http://query.nytimes.com/gst/sitesearch_selector.html" enctype="application/x-www-form-urlencoded">
<input id="hpSearchQuery" name="query" class="text"/>
<input type="hidden" name="type" value="nyt"/>
<input id="searchSubmit" title="Search" width="40" height="19" alt="Search" type="image" src="http://graphics8.nytimes.com/images/global/global_search/search_button40x19.gif">
</form>
</div>

<div id="HPSiteSearch" style="display:none;"></div>
</div>
</div>
<div id="toolsHome">

<a href="http://www.nytimes.com/weather">Personalize Your Weather</a>
</div>
<div class="socialMediaModule">
<p class="listLabel">Follow Us</p>
<ul class="socialMediaTools flush"><li class="facebook"><a href="http://facebook.com/nytimes"><img class="facebookIcon" src="http://graphics8.nytimes.com/images/article/functions/facebook.gif" alt="Facebook"></a></li><li class="twitter"><a href="http://twitter.com/nytimes"><img class="twitterIcon" src="http://graphics8.nytimes.com/images/article/functions/twitter.gif" alt="Twitter"></a></li></ul>
<span class="pipe">|</span>
</div>
</div><!--end #toolbar -->

<div class="singleAd" id="Top">
<!-- ADXINFO classification="Doublebill" campaign="Sony-Monuments-Men-1905167" priority="9000" isInlineSafe="N" width="970" height="250" --><div>

<script type="text/javascript" src="http://graphics8.nytimes.com/ads/javascript/CookieUtil.js?b"></script>

<link rel="stylesheet" type="text/css" href="http://graphics8.nytimes.com/ads/css/doublebillclosebutton2.css" />

</div>
<SCRIPT type="text/javascript" SRC="http://ad.doubleclick.net/adj/N5811.6440.THENEWYORKTIMESCOMPAN/B7866441.2;sz=970x250;pc=nyt232917A362867;ord=2014.02.05.04.43.42?;click=http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=Top&camp=Sony-Monuments-Men-1905167&ad=Homepage-DoublebillRoadblockTuesday2-4-104757468&sn2=4ae2a1a8/f0b66a39&snr=doubleclick&snx=1391571156&sn1=3993977f/e04af4ad&goto=">
</SCRIPT>
<NOSCRIPT>
<A HREF="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=Top&sn2=4ae2a1a8/f0b66a39&sn1=964a7aac/67ce1d0c&camp=Sony-Monuments-Men-1905167&ad=Homepage-DoublebillRoadblockTuesday2-4-104757468&goto=http://ad.doubleclick.net/jump/N5811.6440.THENEWYORKTIMESCOMPAN/B7866441.2;sz=970x250;pc=nyt232917A362867;ord=2014.02.05.04.43.42?" TARGET="_blank">
<IMG SRC="http://ad.doubleclick.net/ad/N5811.6440.THENEWYORKTIMESCOMPAN/B7866441.2;sz=970x250;pc=nyt232917A362867;ord=2014.02.05.04.43.42?"
 BORDER=0 WIDTH=970 HEIGHT=250
 ALT="Click Here"></A>
</NOSCRIPT>

<div id="dbcloseBtn">

<a href="http://www.nytimes.com/ " class="minimizeAd" title="Minimize these advertisements.">Collapse Ad</a> 

</div>

 

<script>

NYTD.AdClose = (function($) {

 

  $('#dbcloseBtn').click(function() {

    $('#Top').css("display", "none");

    $('#dbcloseBtn').css("display", "none");

    CookieUtil.set("NYT-close", "true", new Date("February 5, 2014"));

  });

 

})(NYTD.jQuery);

</script>

<!--MOAT Standard Analytics Code starts here--> 
 <script src="http://js.moatads.com/nyt952824751/moatad.js#moatClientLevel1=Studios&moatClientLevel2=Sony&moatClientLevel3=Sony-Monuments-Men-1905167&moatClientLevel4=Homepage-DoublebillRoadblockTuesday2-4-104757468&moatClientSlicer1=homepage.nytimes.com/index.html&zMoatAT=Standard" type="text/javascript"></script><noscript class="MOAT-nyt952824751?moatClientLevel1=Studios&moatClientLevel2=Sonyamp;moatClientLevel3=Sony-Monuments-Men-1905167&&moatClientLevel4=Homepage-DoublebillRoadblockTuesday2-4-104757468&moatClientSlicer1=homepage.nytimes.com/index.html&zMoatAT=Standard"></noscript> 
 <!--MOAT Standard Analytics Code ends here-->
</div>


<div id="main">
<div id="spanWholePageRegion">
<div class="columnGroup first">				
<style><!--
body #insideNYTimes #insideNYTimesBrowser .story {padding: 0 5px !important;} 

hr, .singleRuleDivider, .doubleRuleDivider{
margin-top: 10px;
margin-bottom: 6px;
}

hr, .singleRuleDivider {
height: 1px;
padding: 0;
background: #e2e2e2;
border: 0;
line-height: 0;
overflow: hidden;
}

--></style>	<style type="text/css"><!--

#TopLeft img[height="1"],
  #TopRight img[height="1"] {
    display: none;
  }

#TopLeft, #TopRight { height: 90px; } 

#TopLeft .prWrap,
#TopRight .prWrap {
width: auto !important;
}

hr, .singleRuleDivider, .doubleRuleDivider{
margin-top: 10px;
margin-bottom: 6px;
}

hr, .singleRuleDivider {
height: 1px;
padding: 0;
background: #e2e2e2;
border: 0;
line-height: 0;
overflow: hidden;
}

--></style>
<script type="text/javascript">
var NYTD=NYTD||{};
</script>	</div>
</div><!--close spanWholePageRegion -->
<div class="baseLayout wrap">
<div class="nav column">
<div class="hpLeftnav" id="HPLeftNav">
<div class="columnGroup fullWidth">
<div class="navigationHomeLede">
<ul class="flush featured">
<li id="navWorld"><a href="http://www.nytimes.com/pages/world/index.html">World</a></li>
<li id="navUS"><a href="http://www.nytimes.com/pages/national/index.html">U.S.</a></li>
<li id="navPolitics"><a href="http://www.nytimes.com/pages/politics/index.html">Politics</a></li>
<li id="navNYRegion"><a href="http://www.nytimes.com/pages/nyregion/index.html">New York</a></li>
<li id="navBusiness"><a href="http://www.nytimes.com/pages/business/index.html">Business</a></li>
<li id="navDealbook"><a href="http://dealbook.nytimes.com">Dealbook</a></li>
<li id="navTechnology"><a href="http://www.nytimes.com/pages/technology/index.html">Technology</a></li>
<li id="navSports"><a href="http://www.nytimes.com/pages/sports/index.html">Sports</a></li>
<li id="navScience"><a href="http://www.nytimes.com/pages/science/index.html">Science</a></li>
<li id="navHealth"><a href="http://www.nytimes.com/pages/health/index.html">Health</a></li>
<li id="navArts"><a href="http://www.nytimes.com/pages/arts/index.html">Arts</a></li>
<li id="navStyle"><a href="http://www.nytimes.com/pages/style/index.html">Style</a></li>
<li id="navOpinion"><a href="http://www.nytimes.com/pages/opinion/index.html">Opinion</a></li>
</ul>
</div>
</div>
<div class="columnGroup">
<div class="navigationHome">
<ul class="flush primary">
<li class="firstItem singleRule">
<ul class="secondary">
<li><a href="http://www.nytimes.com/pages/automobiles/index.html">Autos</a></li>
<li><a href="http://www.nytimes.com/ref/topnews/blog-index.html">Blogs</a></li>
<li><a href="http://www.nytimes.com/pages/books/index.html">Books</a></li>
<li><a href="http://wordplay.blogs.nytimes.com/cartoons/">Cartoons</a></li>
<li><a href="http://www.nytimes.com/ref/classifieds/?incamp=hpclassifiedsnav">Classifieds</a></li>
<li><a href="http://www.nytimes.com/crosswords/index.html">Crosswords</a></li>
<li><a href="http://www.nytimes.com/pages/dining/index.html">Dining &amp; Wine</a></li>
<li><a href="http://www.nytimes.com/pages/education/index.html">Education</a></li>
<li><a href="http://www.nytimes.com/events/">Event Guide</a></li>
<li><a href="http://www.nytimes.com/pages/fashion/index.html">Fashion &amp; Style</a></li>
<li><a href="http://www.nytimes.com/pages/garden/index.html">Home &amp; Garden</a></li>
<li><a href="http://jobmarket.nytimes.com/pages/jobs/">Jobs</a></li>
<li><a href="http://www.nytimes.com/pages/magazine/index.html">Magazine</a></li>
<li><a href="http://www.nytimes.com/pages/business/media/index.html">Media</a></li>
<li><a href="http://www.nytimes.com/pages/movies/index.html">Movies</a></li>
<li><a href="http://www.nytimes.com/pages/arts/music/index.html">Music</a></li>
<li><a href="http://www.nytimes.com/pages/obituaries/index.html">Obituaries</a></li>
<li><a href="http://publiceditor.blogs.nytimes.com/">Public Editor</a></li>
<li><a href="http://www.nytimes.com/pages/realestate/index.html">Real Estate</a></li>
<li><a href="http://www.nytimes.com/pages/opinion/index.html#sundayreview">Sunday Review</a></li>
<li><a href="http://www.nytimes.com/pages/t-magazine/index.html">T Magazine</a></li>
<li><a href="http://www.nytimes.com/pages/arts/television/index.html">Television</a></li>
<li><a href="http://www.nytimes.com/pages/theater/index.html">Theater</a></li>
<li><a href="http://travel.nytimes.com">Travel</a></li>
<li><a href="http://www.nytimes.com/pages/fashion/weddings/index.html">Weddings / Celebrations</a></li>
</ul>
</li>
<li class="singleRule">
<h6 class="kickerBd">Multimedia</h6>
<ul class="secondary">
<li><a href="http://www.nytimes.com/pages/multimedia/index.html">Interactives</a></li>
<li><a href="http://lens.blogs.nytimes.com/">Photography</a></li>
<li><a href="http://video.nytimes.com/">Video</a></li>
</ul>
</li>
<li class="singleRule">
<h6 class="kickerBd">Tools &amp; more</h6>
<ul class="secondary">
<li><a href="https://myaccount.nytimes.com/mem/tnt.html">Alerts</a></li>
<li><a href="http://beta620.nytimes.com/">Beta 620</a></li>
<li><a href="http://www.nytimes.com/pages/corrections/index.html">Corrections</a></li>
<li><a href="http://www.nytimes.com/nytmobile/">Mobile</a></li>
<li><a href="http://movies.nytimes.com/movies/showtimes.html">Movie Tickets</a></li>
<li><a href="http://www.nytimes.com/learning/index.html">Learning Network</a></li>
<li><a href="http://www.nytimes.com/marketing/newsletters/">Newsletters</a></li>
<li><a href="http://nytimes.whsites.net/timestalks/">NYT Events</a></li>
<li><a href="http://www.nytimes.com/nytstore/?utm_source=nytimes&utm_medium=HPB&utm_content=services_blk&utm_campaign=NYT-HP">NYT Store</a></li>
<li><a href="http://theater.nytimes.com/gst/theater/tabclist.html">Theater Tickets</a></li>
<li><a href="http://timesmachine.nytimes.com/">Times Machine</a></li>
<li><a href="http://www.nytimes.com/timesskimmer/">Times Skimmer</a></li>
<li><a href="http://www.nytimes.com/pages/topics/">Times Topics</a></li>
<li><a href="http://www.nytimes.com/timeswire">Times Wire</a></li>
</ul>
</li>
<li class="singleRule">
<h6 class="kickerBd">Subscriptions</h6>
<ul class="flush secondary multiline">
<li><a href="http://www.nytimes.com/hdleftnav">Home Delivery</a></li>
<li><a href="http://www.nytimes.com/digitalleftnav">Digital Subscriptions</a></li>
<li><a href="http://www.nytimes.com/giftleftnav">Gift Subscriptions</a></li>
<li><a href="http://www.nytimes.com/corporateleftnav">Corporate Subscriptions</a></li>
<li><a href="http://www.nytimes.com/educationleftnav">Education Rate</a></li>
<li><a href="http://www.nytimes.com/crosswordsleftnav">Crosswords</a></li>
<li><a href="http://homedelivery.nytimes.com/HDS/HDSHome.do?mode=HDSHome">Home Delivery Customer Care</a></li>
<li><a href="http://eedition.nytimes.com/cgi-bin/signup.cgi?cc=37FYY">Replica Edition</a></li>
<li><a href="https://subscribe.inyt.com">INYT Home Delivery</a></li>
</ul>
</li>
<li class="lastItem singleRule">
<h6 class="kickerBd">Company info</h6>
<ul class="secondary multiline">
<li><a href="http://www.nytco.com/">About NYT Co.</a></li>
<li><a href="http://www.nytimes.whsites.net/mediakit/">Advertise</a></li>
</ul>
</li>
</ul>
</div><!--close navigationHome -->
</div><!--close columnGroup -->
</div>	<div class="columnGroup singleRule">				


</div>  
&nbsp;
</div><!--close nav -->




<div id="spanABCRegion" class="abcColumn opening">
<div class="columnGroup first">				
<style type="text/css">
.alertsContainer { margin-left: 10px; margin-right: 9px; padding: 0; border-top: none; margin-top: 0px; }
body.globalEditionHome .alertsContainer { border-top: 1px solid #797979; margin: -1px 0 0 0; padding: 0 9px 0 10px; }
#alertsRegion { font-family: 'nyt-franklin', Arial, sans-serif; color:#808080; }
.wf-loading #alertsRegion { visibility: hidden; }
#alertsRegion h2 { font-size:1.5em; line-height:1.4em; margin-bottom: .0667em; }
#alertsRegion h2 a {color: black; }
#alertsRegion .summary, #alertsRegion li { font-size:1.3em; line-height: 1.31em;  width: 580px;  background-position: left .55em; }
#alertsRegion p { margin-bottom: 1px; }
#alertsRegion li {margin-bottom: .2em; }
#alertsRegion li:last-child {margin-bottom: 0; }
.newsAlert td, .breakingNewsAlert tr td { padding: 4px 0 8px 0; }
.newsAlertMeta, .breakingNewsAlert td.breakingNewsAlertMeta { padding-top: 9px; }
</style>
<div id="extendedNewsAlertText" style="display:none"><dl>

<dt class='headline'>U.S. Capitol Is Locked Down After Reports of Gunfire

</dt>

<dd class='summary'>Witnesses reported hearing gunshots outside the Capitol after 2 p.m., sparking a huge police response and heightened security inside the Capitol, which was already tense during shutdown negotiations. Members not near their own offices were asked to go to the nearest office, and shelter there.

</dd>

<dd class='bullet'>

</dd>

<dd class='bullet'>

</dd>

<dd class='bullet'>

</dd>

</dl></div>
<script type="text/javascript">
(function($) {
  var run = function() {
    var matchingHeadline = $.trim($("#extendedNewsAlertText > dl > dt.headline").text());
    $("#alertsRegion .breakingNewsAlert h2").each(function(i, alertNode) {
      if($.trim($(alertNode).text()) == matchingHeadline) {
        $("#extendedNewsAlertText > dl > dd.summary").each(function(i, summaryNode) {
          $(alertNode).parent().append("<p class='summary'>" + $(summaryNode).html() + "</p>");
        });
        var ul = null;
        $("#extendedNewsAlertText > dl > dd.bullet").each(function(i, bulletNode) {
          if ($.trim($(bulletNode).html()) != "") {
            if(ul == null) {
              ul = $("<ul></ul>");
              $(alertNode).parent().append(ul);
            }
            ul.append("<li>" + $(bulletNode).html() + "</li>");
          }
        });
      }
    });
  };
  $("#spanABCRegion").removeClass("opening");
  if($("#alertsRegion .breakingNewsAlert h2").length > 0) {
    run();
  } else {
    $(run);
  }
  $(function() {
    if($("#spanABCRegion .columnGroup div").not($("#extendedNewsAlertText")).length > 0) {
      $("#spanABCRegion").addClass("opening");
    }
  });
})(NYTD.jQuery);
</script>	</div>
</div><!--close abcColumn -->
<div class="column last">
<div class="spanAB">
<div class="abColumn">

<!--start lede package -->
<div class="wideB module">
<div class="aColumn opening">
<div class="columnGroup first">				
<div class="story">
<h2><a href="http://www.nytimes.com/2014/02/05/us/politics/budget-office-revises-estimates-of-health-care-enrollment.html?hp">
Health Law Is
Seen as Leading
Some to Leave
Work Force</a></h2>
<h6 class="byline">
By ANNIE LOWREY and JONATHAN WEISMAN        <span class="timestamp" data-eastern-timestamp=" 8:29 PM" data-utc-timestamp="1391563741000"></span>
</h6>
<p class="summary">
The expansion of insurance coverage will lead to a reduction of work hours,  totaling the equivalent of 2.5 million full-time positions by 2024, according to a report.    </p>
<ul class="refer commentsRefer">
<li  style="background-image: none; padding-left: 0pt;"><span class="commentCountLink" articleid="http://www.nytimes.com/2014/02/05/us/politics/budget-office-revises-estimates-of-health-care-enrollment.html" overflowurl="http://community.nytimes.com/comments/www.nytimes.com/2014/02/05/us/politics/budget-office-revises-estimates-of-health-care-enrollment.html?hp&target=comments" articletitle="Health Law Is
Seen as Leading
Some to Leave
Work Force"></span></li>
</ul>
</div>
<div class="singleRuleDivider"></div>	</div>
<div class="columnGroup ">				
<div class="story">
<h3><a href="http://www.nytimes.com/2014/02/05/us/politics/senate-passes-long-stalled-farm-bill.html?hp">
Senate Passes Farm Bill With Clear Winners and Losers</a></h3>
<h6 class="byline">
By RON NIXON        <span class="timestamp" data-eastern-timestamp=" 8:34 PM" data-utc-timestamp="1391564093000"></span>
</h6>
<p class="summary">
Over all, agribusiness fared far better than the poor in the long-stalled farm bill, which represents nearly $1 trillion in spending over the next 10 years and passed on a rare bipartisan vote.    </p>
<ul class="refer commentsRefer">
<li  style="background-image: none; padding-left: 0pt;"><span class="commentCountLink" articleid="http://www.nytimes.com/2014/02/05/us/politics/senate-passes-long-stalled-farm-bill.html" overflowurl="http://community.nytimes.com/comments/www.nytimes.com/2014/02/05/us/politics/senate-passes-long-stalled-farm-bill.html?hp&target=comments" articletitle="Senate Passes Farm Bill With Clear Winners and Losers"></span></li>
</ul>
</div>
<div class="singleRuleDivider"></div>	</div>
<div class="columnGroup ">				
<div class="story">
<h3><a href="http://www.nytimes.com/2014/02/05/us/politics/republicans-spar-on-leaks-and-surveillance-underscoring-partisan-shake-up.html?hp">
Republicans Spar on Leaks and Secret Surveillance</a></h3>
<h6 class="byline">
By CHARLIE SAVAGE        <span class="timestamp" data-eastern-timestamp=" 8:33 PM" data-utc-timestamp="1391564039000"></span>
</h6>
<p class="summary">
House Republicans offered sharply divergent views about secret surveillance programs and the leaks that made them public, underscoring the unsettled nature of a political debate that has scrambled the usual partisan lines.    </p>
<ul class="refer commentsRefer">
<li><a href="http://www.nytimes.com/2014/02/05/books/the-snowden-files-by-luke-harding.html">Books of The Times: 'The Snowden Files'</a></li>
</ul>
</div>
<div class="singleRuleDivider"></div>	</div>
<div class="columnGroup last">				
<h6 class="kicker">More News</h6>
<div class="story">
<ul class="headlinesOnly">
<li>
<h5><a href="http://www.nytimes.com/2014/02/05/nyregion/test-of-substance-in-hoffmans-home-finds-heroin-without-additive.html?hp">
No Additive in Heroin Found in Hoffman’s Home</a>
<span class="timestamp" data-eastern-timestamp="10:22 PM" data-utc-timestamp="1391570522000"></span>
</h5>
</li>
<li>
<h5><a href="http://www.nytimes.com/2014/02/05/nyregion/de-blasio-to-skip-st-patricks-day-parade-cites-exclusion-of-gay-groups.html?hp">
De Blasio to Skip St. Patrick’s Day Parade</a>
</h5>
</li>
<li>
<h5><a href="http://www.nytimes.com/2014/02/05/us/politics/obama-announces-pledges-of-750-million-for-student-technology.html?hp">
$750 Million Pledged for Student Technology</a>
<span class="timestamp" data-eastern-timestamp=" 2:20 PM" data-utc-timestamp="1391541639000"></span>
</h5>
</li>
<div style="margin-top: -6px;"></div>           </ul>
</div>
</div>
</div><!--close aColumn -->
<div class="bColumn opening">
<div id="photoSpotRegion">
<div class="columnGroup first">				
<script>function getFlexData() { return {"data":{"backgroundImage":"http:\/\/graphics8.nytimes.com\/images\/2014\/01\/29\/multimedia\/berlin-teufelsberg-nsa\/berlin-teufelsberg-nsa-videoHpMedium-v2.jpg","photoCredit":"Erik Olsen","shareURL":"http:\/\/www.nytimes.com\/2014\/02\/05\/world\/europe\/where-nsa-kept-watch-in-cold-war-artists-now-find-refuge.html","videoID":100000002678359}}; }var NYTD=NYTD || {}; NYTD.FlexTypes = NYTD.FlexTypes || []; NYTD.FlexTypes.push({"target":"FT100000002689065","type":"HP5 Video Embed 375","data":{"backgroundImage":"http:\/\/graphics8.nytimes.com\/images\/2014\/01\/29\/multimedia\/berlin-teufelsberg-nsa\/berlin-teufelsberg-nsa-videoHpMedium-v2.jpg","photoCredit":"Erik Olsen","shareURL":"http:\/\/www.nytimes.com\/2014\/02\/05\/world\/europe\/where-nsa-kept-watch-in-cold-war-artists-now-find-refuge.html","videoID":100000002678359}});</script><style><!--
div#photospotVideoPlayerCreditContainer {height:16px;}
.ledePhoto {display:none;}
--></style>
<div id="photospotVideoPlayerContainer" style="height: 211px; width: 375px; background-color: rgb(39, 39, 39);"></div>
<div id="photospotVideoPlayerCreditContainer">
<h6 class="credit" id="photospotVideoPlayerCredit"></h6>
</div>
<script type="text/javascript" src="http://js.nyt.com/js2/build/video/2.0/videofactory.js"></script>
<script type='text/javascript'>
(function() {

       var hpVideoEmbedFlexData = getFlexData().data;

	NYTD.Video.Factory.loadDependencies(function(success) {
		var video = NYTD.Video.Factory.create({
			container: 'photospotVideoPlayerContainer',
			id: 'photospotVideoPlayer',
			playerId: '2028569413001',
			videoId: hpVideoEmbedFlexData.videoID,
			width: 375,
			height: 211,
			autoStart: false,
			autoRender: false,
			playerType: 'photospot',
			bgcolor: '#000000',
			quality: 'high',
			shareURL: hpVideoEmbedFlexData.shareURL,
			overlay: {
				backgroundImage: hpVideoEmbedFlexData.backgroundImage,
				bumper: '',
				buttonPosition: 'bottomLeft', // where to anchor the button
				buttonAnimated: true, // should the button animate
				buttonExpandBy: 80, // how wide should the button animate
				buttonFontColor: '#FFF', // color of the text in the button
				buttonFontSize: '12px', // size of the text in the button
				buttonPaddingLeftRight: 20,
				buttonPaddingTopBottom: 20,
				photoCredit: hpVideoEmbedFlexData.photoCredit,
				photoCreditContainer: "photospotVideoPlayerCredit"
			}
		});
	});
})();
</script>
<div id="FT100000002689065"></div><div class="story">
<div class="ledePhoto" id="ledePhoto">
<div class="image">
<a href="http://www.nytimes.com/2014/02/05/world/europe/where-nsa-kept-watch-in-cold-war-artists-now-find-refuge.html?hp"><img src="http://i1.nyt.com/images/2014/01/29/multimedia/berlin-teufelsberg-nsa/berlin-teufelsberg-nsa-largeHorizontal375.jpg" width="375" height="250" alt="" /></a>
</div>
<h6 class="credit">Erik Olsen</h6>
</div>
<h3><a href="http://www.nytimes.com/2014/02/05/world/europe/where-nsa-kept-watch-in-cold-war-artists-now-find-refuge.html?hp">
Artists Find Refuge in Cold War Ruins</a></h3>
<h6 class="byline">
By MELISSA EDDY        <span class="timestamp" data-eastern-timestamp=" 9:05 PM" data-utc-timestamp="1391565945000"></span>
</h6>
<p class="summary">
More than two decades after the United States pulled up its final cables from Field Station Berlin, the complex still holds a mystical attraction for history buffs, artists and tourists.        </p>
</div>
</div>
</div>
<div class="doubleRuleDivider insetH"></div>   
<div class="columnGroup first">				
<div class="story">
<h5><a href="http://www.nytimes.com/2014/02/05/world/europe/entrusted-to-burn-john-paul-iis-notes-cardinal-publishes-them-instead.html?hp">
Cardinal Publishes Pope John Paul II’s Notes</a></h5>
<h6 class="byline">
By DAN BILEFSKY        <span class="timestamp" data-eastern-timestamp="11:11 PM" data-utc-timestamp="1391573476000"></span>
</h6>
<p class="summary">
Cardinal Stanislaw Dziwisz, who was the pontiff’s secretary,  defied the pope’s order in his will to burn his notes.    </p>
</div>
<div class="singleRuleDivider"></div>	</div>
<div class="columnGroup ">				
<div class = "story">
<h5><a href = "http://www.nytimes.com/2014/02/05/world/asia/philippine-leader-urges-international-help-in-resisting-chinas-sea-claims.html?hp">
Philippines Seeks Help on China’s Sea Claims</a></h5>
<div class = "thumbnail runaroundRight" style = "margin-top: 4px">
<a href = "http://www.nytimes.com/2014/02/05/world/asia/philippine-leader-urges-international-help-in-resisting-chinas-sea-claims.html?hp">
<img src = "http://i1.nyt.com/images/2014/02/04/multimedia/aquino-interview/aquino-interview-thumbStandard-v4.jpg" width = "75" 
            height = "75" 
            alt = "Benigno S. Aquino III, the Philippine president." border = "0" />
</a>
</div>
<h6 class = "byline">
By KEITH BRADSHER        <span class="timestamp" data-eastern-timestamp=" 5:25 PM" data-utc-timestamp="1391552711000"></span>
</h6>
<p class="summary">
Benigno S. Aquino III, the Philippine president, compared China’s claims to the seas near his country to Hitler’s demands for Czech land in 1938.    </p>
<ul class = "refer commentsRefer">
<li  style = "background-image: none; padding-left: 0pt;">
<span class = "commentCountLink" articleid = "http://www.nytimes.com/2014/02/05/world/asia/philippine-leader-urges-international-help-in-resisting-chinas-sea-claims.html" 
                                overflowurl = "http://community.nytimes.com/comments/2014/02/05/world/asia/philippine-leader-urges-international-help-in-resisting-chinas-sea-claims.html?hp&target=comments" articletitle="Philippines Seeks Help on China’s Sea Claims"></span>
</li>
</ul>
</div>	</div>
<div class="columnGroup ">				
<div class="singleRuleDivider"></div>
<div class = "story">
<h5><a href = "http://www.nytimes.com/2014/02/05/education/tennessee-governor-urges-2-free-years-of-community-college-and-technical-school.html?hp">
Tennessee Proposes 2 Years of Free College Courses</a></h5>
<div class = "thumbnail runaroundRight" style = "margin-top: 4px">
<a href = "http://www.nytimes.com/2014/02/05/education/tennessee-governor-urges-2-free-years-of-community-college-and-technical-school.html?hp">
<img src = "http://i1.nyt.com/images/2014/02/05/us/TENNESSEE/TENNESSEE-thumbStandard-v2.jpg" width = "75" 
            height = "75" 
            alt = "Gov. Bill Haslam, left, with legislators on Monday night in Nashville, proposed bolstering Tennessee’s work force  with two years of free schooling." border = "0" />
</a>
</div>
<h6 class = "byline">
By RICHARD PÉREZ-PEÑA        <span class="timestamp" data-eastern-timestamp=" 8:26 PM" data-utc-timestamp="1391563602000"></span>
</h6>
<p class="summary">
Tennessee would be the only state in the country to charge no tuition or fees to incoming community college students under the proposal by Gov. Bill Haslam.    </p>
<ul class = "refer commentsRefer">
<li><a href="http://www.nytimes.com/interactive/2014/01/28/us/28-stateofstates.html">State of the States</a></li>
</ul>
</div>	</div>
<div class="columnGroup ">				
<div class="singleRuleDivider"></div>	<div class="story">
<h5><a href="http://www.nytimes.com/2014/02/05/technology/new-boss-at-microsoft-with-gates-at-his-side.html?hp">
New Boss at Microsoft, With Gates at His Side</a></h5>
<h6 class="byline">
By NICK WINGFIELD        <span class="timestamp" data-eastern-timestamp=" 8:59 PM" data-utc-timestamp="1391565544000"></span>
</h6>
<p class="summary">
Bill Gates will return part-time to the company after the new chief executive, Satya Nadella, asked him to be his adviser.    </p>
</div>
<div class="singleRuleDivider"></div>	</div>
<div class="columnGroup last">				
<style>
	#nytDesignSochiHeaderWideCenter {
		margin-bottom: 8px;
		text-align: center;
		}
	#nytDesignSochiHeaderWideCenter h6 {
		display: inline-block;
		position: relative;
		margin: 0 auto;
		padding: 0 8px;
		text-transform: uppercase;
		font-size: 13px;
		font-weight: 700;
		letter-spacing: 1px;
		font-family: nyt-franklin,arial,helvetica,sans-serif;
		font-weight: bold;
		}
	#nytDesignSochiHeaderWideCenter h6 a.nytDesignSochiHeaderLink,
	#nytDesignSochiHeaderNarrowLeft h6 a.nytDesignSochiHeaderLink:visited {
		text-decoration: none;
		position: relative;
		margin-bottom: 8px;
		color: #1a1a1a;
		}
	#nytDesignSochiHeaderWideCenter h6 a i {
		position: absolute;
		display: block;
		height: 2px;
		left: -2px;
		bottom: -4px;
		border-left: 21px #257EB8 solid;
		border-right: 22px #E4B05E solid;
		}
	#nytDesignSochiHeaderWideCenter h6 a i.second {
		left: auto;
		right: -2px;
		border-left-color: #22A254;
		border-right-color: #D73A39;
		}
</style>
<div id="nytDesignSochiHeaderWideCenter">
<h6><a class="nytDesignSochiHeaderLink" href="http://www.nytimes.com/pages/sports/olympics/index.html">Sochi 2014<i class="first"></i><i class="second"></i></a></h6>
</div>
<div class = "story">
<h5><a href = "http://www.nytimes.com/2014/02/05/sports/olympics/japan-is-a-land-of-rising-hopes-for-ski-jumping.html?hp">
Japan Is a Land of Rising Hopes for Ski Jumping</a></h5>
<div class = "thumbnail runaroundRight" style = "margin-top: 4px">
<a href = "http://www.nytimes.com/2014/02/05/sports/olympics/japan-is-a-land-of-rising-hopes-for-ski-jumping.html?hp">
<img src = "http://i1.nyt.com/images/2014/02/05/sports/olySKIJUMP1/olySKIJUMP1-thumbStandard.jpg" width = "75" 
            height = "75" 
            alt = "The ski jumper Yuki Ito trained in Nayoro, Japan, last summer." border = "0" />
</a>
</div>
<h6 class = "byline">
By KEN BELSON        <span class="timestamp" data-eastern-timestamp=" 4:52 PM" data-utc-timestamp="1391550730000"></span>
</h6>
<p class="summary">
Japan’s once-thriving ski jumping program is seeking a revival, and Yuki Ito and Sara Takanashi have a key role as their sport makes its Olympic debut for women.    </p>
</div><style>
	.nytDesignSochiEmail {
		font-family: "nyt-franklin",helvetica,arial,sans-serif;
		font-size: 10px;
		font-weight: 500;
		text-align: center;
	}
	
		.nytDesignSochiEmail .singleRuleDivider {
			width: 50%;
			margin: 12px auto;
		}
		
		.nytDesignSochiEmail a,
		.nytDesignSochiEmail a:visited,
		.nytDesignSochiEmail a:hover,
		.nytDesignSochiEmail a:active {
			color: #909090;
			text-decoration: none;
		}
		
		.nytDesignSochiEmail a strong {
			display: inline-block;
			font-weight: 500;
			color: #326891;
		}
		
			.nytDesignSochiEmail a:hover strong {
				text-decoration: underline;
			}
		
		.nytDesignSochiEmail .icon {
			position: relative;
			top: -1px;
			padding-top: 1px;
		}
		
		.nytDesignSochiEmail .emailAlert {
			background-image: url('http://graphics8.nytimes.com/packages/images/nytdesign/2014/olympics/homepage/icons/icon-media-email-alert-12x12-6389A5.gif');
		}
			
			.nytDesignSochiEmail a:hover .emailAlert {
				background-image: url('http://graphics8.nytimes.com/packages/images/nytdesign/2014/olympics/homepage/icons/icon-media-email-alert-12x12-326891.gif');
			}
		
</style>
<div class="nytDesignSochiEmail">
<div class="singleRuleDivider"></div>
<p><a href="http://sochi2014.nytimes.com/email?hp"><span class="media icon emailAlert"> </span>Sign up for a <strong>daily recap</strong> of highlights from the Winter Games.</a></p>
</div>	</div>
</div><!--close bColumn -->
</div><!--close wideB -->  
<div id="spanABBottomRegion">
<div class="columnGroup first">				
<div class="doubleRuleDivider"></div>	<div style="margin-top:10px"></div>	<script>function getFlexData() { return {"data":{"1":{"url":"http:\/\/www.nytimes.com\/news\/minute\/2014\/02\/04\/times-minute-army-recruitment-scam","hed":"Territorial Dispute","img":"http:\/\/graphics8.nytimes.com\/images\/2014\/02\/04\/world\/islands-dispute-minute\/islands-dispute-minute--videoHpMedium.jpg"},"2":{"url":"http:\/\/www.nytimes.com\/news\/minute\/2014\/02\/04\/times-minute-army-recruitment-scam","hed":"Army Recruitment Scam","img":"http:\/\/graphics8.nytimes.com\/images\/2014\/02\/04\/pageoneplus\/Army-Recruit\/Army-Recruit-videoHpMedium.jpg"},"3":{"url":"http:\/\/www.nytimes.com\/news\/minute\/2014\/02\/04\/times-minute-army-recruitment-scam","hed":"Health Care Report","img":"http:\/\/graphics8.nytimes.com\/images\/2014\/02\/05\/us\/05health_top\/05health_top-videoHpMedium.jpg"},"timestamp":"","url":"http:\/\/www.nytimes.com\/news\/minute\/2014\/02\/04\/times-minute-army-recruitment-scam","rotation":true}}; }var NYTD=NYTD || {}; NYTD.FlexTypes = NYTD.FlexTypes || []; NYTD.FlexTypes.push({"target":"FT100000002688334","type":"TimesMinute Rotating Promo","data":{"1":{"url":"http:\/\/www.nytimes.com\/news\/minute\/2014\/02\/04\/times-minute-army-recruitment-scam","hed":"Territorial Dispute","img":"http:\/\/graphics8.nytimes.com\/images\/2014\/02\/04\/world\/islands-dispute-minute\/islands-dispute-minute--videoHpMedium.jpg"},"2":{"url":"http:\/\/www.nytimes.com\/news\/minute\/2014\/02\/04\/times-minute-army-recruitment-scam","hed":"Army Recruitment Scam","img":"http:\/\/graphics8.nytimes.com\/images\/2014\/02\/04\/pageoneplus\/Army-Recruit\/Army-Recruit-videoHpMedium.jpg"},"3":{"url":"http:\/\/www.nytimes.com\/news\/minute\/2014\/02\/04\/times-minute-army-recruitment-scam","hed":"Health Care Report","img":"http:\/\/graphics8.nytimes.com\/images\/2014\/02\/05\/us\/05health_top\/05health_top-videoHpMedium.jpg"},"timestamp":"","url":"http:\/\/www.nytimes.com\/news\/minute\/2014\/02\/04\/times-minute-army-recruitment-scam","rotation":true}});</script><link rel="stylesheet" type="text/css" href="http://graphics8.nytimes.com/packages/js/nytint/projects/times_minute/timesminute.css?v1.7" />
<script type="text/html" id="timesminute">
  <div id="timesMinuteContainer">
    <div class="story">
      <a href="#">
        <div class="thumbnail runaroundLeft">
          <img src="http://graphics8.nytimes.com/images/misc/spacer.gif">
          <div class="vidOverlay"></div>
          <hr />
        </div>
        <h5><nobr>Times <span>Minute</span></nobr> <span class="timestamp"></span></h5>
        <ul class="flush"><li></li><li></li><li></li></ul>
      </a>
    </div>
  </div>
</script>
<script type="text/html" id="timesminuteAB">
  <div id="timesMinuteContainer">
    <div class="story">
      <a href="#">
        <div class="lede">
          <h5>Times <span>Minute</span> <span class="timestamp"></span></h5>
          <p>Catch up on the day’s news, in 60 seconds.</p> 
        </div>
        <ul class="flush">
          <li>
            <div class="thumbnail">
              <img src="http://graphics8.nytimes.com/images/misc/spacer.gif">
              <div class="vidOverlay"></div>
            </div>
          </li>
          <li>
            <div class="thumbnail">
              <img src="http://graphics8.nytimes.com/images/misc/spacer.gif">
              <div class="vidOverlay"></div>
            </div>
          </li>
          <li>
            <div class="thumbnail">
              <img src="http://graphics8.nytimes.com/images/misc/spacer.gif">
              <div class="vidOverlay"></div>
            </div>
          </li>
        </ul>
      </a>
    </div>
  </div>
</script>
<script src="http://typeface.nytimes.com/miq8eej.js" type="text/javascript" async=""></script>
<script src="http://graphics8.nytimes.com/packages/js/nytint/projects/times_minute/flextype_scriptsrc.js?v1.7" type="text/javascript"></script><div id="FT100000002688334"></div>	<div style="margin-top:10px"></div>	</div>
</div><!--close spanABBottomRegion -->
<div class="wideA">
<div class="aColumn">
<div class="columnGroup doubleRule">
<div id="extendedVideoPlayerModule" class="extendedVideoPlayerModule extendedVideoPlayerLegacyModule">
<div class="extVidPlayerHeader clearfix">
<a href="http://www.nytimes.com/video/" class="extVidPlayerMainHeaderLink">Video &raquo;</a>
<a href="http://www.nytimes.com/video?src=vidm" class="extVidPlayerSectionHeaderLink" target="_blank"> More Video &raquo;</a>
</div>
<div class="videoContainer">
<div class="extendedVideoPocketPlayerContainer"></div>
<div class="videoShare shareTools shareToolsThemeClassic shareToolsThemeClassicHorizontal slideshowShareTools" 
            data-shares="showall|Share,email|E-mail,twitter|Twitter,facebook|Facebook" 
            data-url="" 
            data-title="" 
            data-description="">
</div>
<div class="videoDetails">
<p class="kicker"></p>
<a href="#" class="shortDescription" target="_blank"></a>
<p class="longDescription"></p>
</div>
</div>
<div class="extVidPlayerThumbsContainer">
<div class="extVidPlayerThumbsContainerShadow"></div>
<div class="extVidPlayerNav clearfix">
<div class="extVidPlayerNavContent clearfix">
<a href="#" class="previousVideo previousVideoInactive">previous</a>
<a href="#" class="nextVideo">next</a>
</div>
</div>
<div id="extVidPlayerThumbsWrapper" class="extVidPlayerThumbsWrapper">
<ul id="extVidPlayerThumbs" class="videoThumbs clearfix"></ul>
</div>
</div>
</div>
<script type="text/javascript" src="http://js.nyt.com/js2/build/video/2.0/videofactory.js"></script>
<script type="text/javascript" src="http://js.nyt.com/js2/build/video/players/extended/1.0/app.js"></script>
<script type="text/javascript">
    var player = new NYTD.video.players.Extended({
        container: "extendedVideoPlayerModule",
        referenceId: "1194811622188",
        thumbWidth: 90,
        videoWidth: '100%',
        videoHeight: '100%'
    });
</script>                                    </div>
</div><!--close aColumn -->
<div class="bColumn">
<div class="columnGroup doubleRule">
<div id="pocketRegion" class="module">
<div class="columnGroup first">				
<style type="text/css"><!--
.hideAllKickers h6.kicker { display: none; }
--></style>
<div class="hideAllKickers story"><div class="story">
<h5><a href="http://www.nytimes.com/2014/02/05/dining/at-bouley-botanical-planters-overflow.html?hp">
At Bouley Botanical, Planters Overflow</a></h5>
<h6 class="byline">
By JEFF GORDINIER        <span class="timestamp" data-eastern-timestamp="12:29 PM" data-utc-timestamp="1391534967000"></span>
</h6>
<div class="thumbnail">
<a href="http://www.nytimes.com/2014/02/05/dining/at-bouley-botanical-planters-overflow.html?hp">
<img src="http://i1.nyt.com/images/2014/02/05/dining/20140205-BOULEY-slide-8LP0/20140205-BOULEY-slide-8LP0-thumbStandard.jpg" width="75" height="75" alt="" border="0" />
</a>
</div>
<p class="summary">
The latest project from the chef David Bouley is a downtown Eden overflowing with herbs, flowers and vegetables.    </p>
<ul class="refer commentsRefer">
<li  style="background-image: none; padding-left: 0pt;"><span class="commentCountLink" articleid="http://www.nytimes.com/2014/02/05/dining/at-bouley-botanical-planters-overflow.html" overflowurl="http://community.nytimes.com/comments/2014/02/05/dining/at-bouley-botanical-planters-overflow.html?hp&target=comments" articletitle="At Bouley Botanical, Planters Overflow"></span></li>
</ul>
</div>
</div>	</div>
<div class="columnGroup ">				
<script type="application/javascript">
  window.NYTD = window.NYTD || {};
  window.NYTD.NYTINT = NYTD.NYTINT || {};
  window.NYTD.NYTINT.OlyHPBug = {};
  window.NYTD.NYTINT.OlyHPBug.settings = {
    active: true,
    polling: true,
    endpoint_diversity: 250
  };
</script>
<script src="http://int.nyt.com/applications/sochi_hub/assets/homepage-bug-a584aafd750fa54cf325b3cc80f189e5.js"></script>	<script>
NYTD.jQuery(".ledePhoto .embeddedSlideshow").css('height', 'inherit');
</script>	</div>
<div class="columnGroup ">				
<div class="singleRuleDivider"></div>	</div>
<div class="columnGroup last">				
<h6 class="kicker"><a href="http://www.nytimes.com/pages/aponline/index.html">News from A.P.</a> & <a href="http://www.nytimes.com/pages/reuters/index.html">Reuters</a> »</h6>
<div class="story">
<h6><a href="http://www.nytimes.com/aponline/2014/02/04/sports/ncaabasketball/ap-bkc-t25-wake-forest-duke.html?hp">
<!---->
Parker, No. 11 Duke Rout Wake Forest, 83-63</a>
</h6>
<span class="timestamp" data-eastern-timestamp="11:31 PM" data-utc-timestamp="1391574708000"></span>
</div>
<div class="story">
<h6><a href="http://www.nytimes.com/aponline/2014/02/04/sports/ncaabasketball/ap-bkc-t25-missouri-florida.html?hp">
<!---->
No. 3 Florida Beats Missouri, Wins 14th Straight</a>
</h6>
<span class="timestamp" data-eastern-timestamp="11:34 PM" data-utc-timestamp="1391574893000"></span>
</div>
<div class="story">
<h6><a href="http://www.nytimes.com/aponline/2014/02/04/us/ap-us-navy-carrier-final-trip.html?hp">
<!---->
Navy Supercarrier Leaves Pa. On Trip to Scrap Heap</a>
</h6>
<span class="timestamp" data-eastern-timestamp="11:25 PM" data-utc-timestamp="1391574356000"></span>
</div>
<div class="story">
<h6><a href="http://www.nytimes.com/aponline/2014/02/04/sports/ap-car-indianapolis-vintage-races.html?hp">
<!---->
Indy Adds Vintage Race Weekend to June Schedule</a>
</h6>
<span class="timestamp" data-eastern-timestamp="11:04 PM" data-utc-timestamp="1391573086000"></span>
</div>
</div>
</div><!--close pocketRegion -->
</div>
</div><!--close bColumn -->
</div><!--close wideA -->
<!--end lede package -->
</div><!--close abColumn -->
<div class="cColumn">


<div id="cColumnTopSpanRegion">
<div class="columnGroup first">				
<div class="opinionModule">
<h4 class="sectionHeaderHome"><a href="http://www.nytimes.com/pages/opinion/?hp"><img src="http://graphics8.nytimes.com/packages/images/nytdesign/2014/opinion/homepage/opinionPagesHpC375.png" /></a>
</h4>
<div class="subColumn-2 wrap layout ">
<div class="column">
<div class="insetH">
<div class="story">
<h5><a href="http://www.nytimes.com/2014/02/05/opinion/freeing-workers-from-the-insurance-trap.html?hp&rref=opinion">Freeing Workers From the Insurance Trap</a>
</h5>
<h6 class="byline">By THE EDITORIAL BOARD</h6>
<p class="summary flushBottom">A new report found that by reducing the number of full-time workers over a decade,
the health care law will have a liberating impact for millions.</p>
<ul class="refer"></ul>
</div>
<h6 class="kicker">Op-Ed Columnists</h6>
<ul class="headlinesOnly">
<li><a href="http://www.nytimes.com/2014/02/05/opinion/dowd-high-school-maniacal.html?hp&rref=opinion">Dowd: High School Maniacal</a>
</li>
<li><a href="http://www.nytimes.com/2014/02/05/opinion/friedman-the-third-intifada.html?hp&rref=opinion">Friedman: A Third Intifada</a>
</li>
</ul>
</div>
</div>
<div class="column lastColumn">
<div class="insetH">
<div class="story">
<h5><a href="http://www.nytimes.com/roomfordebate/2014/02/04/from-shadows-to-citizenship?hp&rref=opinion">From Shadows to Citizenship</a>
</h5>
<div class="thumbnail runaroundRight"><a href="http://www.nytimes.com/roomfordebate/2014/02/04/from-shadows-to-citizenship?hp&rref=opinion"><img src="http://graphics8.nytimes.com/images/2010/07/09/opinion/09rfd-image/09rfd-image-custom4.jpg" height="50" width="50" /></a>
</div>
<p class="summary flushBottom">If immigrants can get legal status, should they be given a path to full civic
rights?</p>
</div>
<ul class="headlinesOnly">
<li><a href="http://www.nytimes.com/2014/02/05/opinion/edsall-free-trade-disagreement.html?hp&rref=opinion">Edsall: Free Trade Disagreement</a>
</li>
<li><a href="http://www.nytimes.com/2014/02/05/opinion/yu-hua-chinas-censorship-pendulum.html?hp&rref=opinion">Yu Hua: China's Censorship Pendulum</a>
</li>
<li><a href="http://www.nytimes.com/2014/02/05/opinion/bittman-just-say-no.html?hp&rref=opinion">Bittman: Just Say No</a>
</li>
</ul>
</div>
</div>
</div>
</div>	<div class="doubleRuleDivider"></div>	</div>
</div><!--close cColumnTopSpanRegion -->


<div class="columnGroup first">				
<div class="columnGroup fullWidth flushBottom">
<div class="subColumn-2 wrap noBackground layout">
<div class="column">
<div class="columnGroup flushBottom">	<script type="text/javascript">
  <!--
    function insertWSODModule(file){
      var doc  = document.getElementsByTagName('head').item(0);
      var rnd  = "?"+ Math.random();
      var wsod = document.createElement('script');
      wsod.setAttribute('language','javascript');
      wsod.setAttribute('type','text/javascript');
      wsod.setAttribute('src',file+rnd);
      doc.appendChild(wsod);
    }
  
  //-->
</script>
<div id="wsodMarkets">
<div id="wsodMarketsChart"></div>
<script type="text/javascript"><!--
insertWSODModule("http://markets.on.nytimes.com/research/modules/home/home.asp");
//--></script>
<form id="wsodFormHome" class="searchForm" method="get" action="http://query.nytimes.com/gst/getquotes.html">
<div><label for="qsearchQuery">Get Quotes</label>
<p id="myPortfolios"><a href="http://markets.on.nytimes.com/research/portfolio/view/view.asp">My Portfolios »</a></p>
<input id="qsearchQuery" name="symb" type="text" onblur="if(this.value=='')this.value='Stock, ETFs, Funds';" onfocus="if(this.value=='Stock, ETFs, Funds')this.value='';" value="Stock, ETFs, Funds" />
<div class="querySuggestions" style="display:none"></div>
<input id="searchSubmit" type="image" src="http://graphics8.nytimes.com/images/global/buttons/go.gif"></div>
</form>
</div>	</div>
</div>
<div class="column lastColumn">
<div class="columnGroup flushBottom">
<div id="Middle4"><!-- ADXINFO classification="Home_Product_Marketplace_Button" campaign="Dell_Jan-March_2014_1912487-nyt2" priority="8000" isInlineSafe="N" width="160" height="60" --><a href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=Middle4&sn2=1523368b/d11e58cc&sn1=3b47a717/f9059c71&camp=Dell_Jan-March_2014_1912487-nyt2&ad=Dell_Office_Marketing_163x90_HPMarkets_010814&goto=http%3A%2F%2Fpaidpost%2Enytimes%2Ecom%2Fdell%2Freaching%2Dacross%2Dthe%2Doffice%2Dfrom%2Dmarketing%2Dto%2Dit%2Ehtml" target="_blank">
<img src="http://graphics8.nytimes.com/adx/images/ADS/36/10/ad.361083/dell_163x90D.gif" width="163" height="90" border="0">
</a></div>

</div>
</div>
</div>
</div>	</div>
<div id="cColumnAboveMothRegion">
<div class="columnGroup first">				

</div>
<div class="columnGroup first">				
<div class="singleRuleDivider"></div>
<div class="columnGroup fullWidth flushBottom">
<div class="subColumn-2 wrap noBackground layout">
<div class="column">
<div class="columnGroup flushBottom">	<div style="margin-top: 2px;"></div>	<h4 class="sectionHeaderHome"><a href="http://www.nytimes.com/pages/arts/index.html?src=dayp">Arts »</a></h4>
<div class="story">
<h5><a href="http://www.nytimes.com/2014/02/05/arts/design/momas-proposal-for-sculpture-garden-pleases-and-riles.html?src=dayp">
MoMA’s Proposal for Sculpture Garden Pleases and Riles
</a></h5>
<div class="runaroundRight">
<a href="http://www.nytimes.com/2014/02/05/arts/design/momas-proposal-for-sculpture-garden-pleases-and-riles.html?src=dayp">
<img src="http://graphics8.nytimes.com/images/2014/02/04/arts/artsspecial/20140205GARDEN-slide-TAP7/20140205GARDEN-slide-TAP7-thumbStandard.jpg" alt="
MoMA’s Proposal for Sculpture Garden Pleases and Riles" width="75" height="75" />
</a></div>
<p class="summary">
The Museum of Modern Art’s plan to allow greater access to its sculpture garden is seen as step forward or backward, depending on the perspective.
</p>
</div>
<div class="story">
<h5><a href="http://www.nytimes.com/2014/02/05/arts/president-of-bam-will-leave-next-year.html?src=dayp">
President of BAM Will Leave Next Year
</a></h5>
<p class="summary">
Karen Brooks Hopkins will step down as president of the Brooklyn Academy of Music in June of next year, after more than 15 years in the job.
</p>
</div>
<!--end of first daypart promo code, don't touch the column code below -->
</div></div><div class="column lastColumn"><div class="columnGroup flushBottom"><h4 class="sectionHeaderHome"> </h4>
<!--- insert second daypart promo below -->
<div class="story">
<h6 class="kicker">Books of The Times</h6>
<h5><a href="http://www.nytimes.com/2014/02/05/books/the-snowden-files-by-luke-harding.html?src=dayp">
Tales From Within the N.S.A.’s Haystack
</a></h5>
<div class="runaroundRight">
<a href="http://www.nytimes.com/2014/02/05/books/the-snowden-files-by-luke-harding.html?src=dayp">
<img src="http://graphics8.nytimes.com/images/2014/02/05/arts/05BOOK/05BOOK-thumbStandard.jpg" alt="Tales From Within the N.S.A.’s Haystack" width="75" height="75" />
</a></div>
<p class="summary">
A reporter collects the pieces of the Edward Snowden story into a book about how the world came to learn about the N.S.A.’s reach.
</p>
<ul class="refer">
<li style="background-image: none; padding-left: 0pt;"><span class="commentCountLink" articleid="http://www.nytimes.com/2014/02/05/books/the-snowden-files-by-luke-harding.html" overflowurl="http://community.nytimes.com/comments/www.nytimes.com/2014/02/05/books/the-snowden-files-by-luke-harding.html?ref=arts&target=comments" articletitle="The Needles in the Monumental N.S.A. Haystack"></span></li>
</ul>
</div>	<div id="Middle5"><!-- ADXINFO classification="Home_Page_Advantage" campaign="Cap_One_360_2014_1912371-nyt1" priority="8000" isInlineSafe="N" width="163" height="90" --><A HREF="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=Middle5&sn2=1523368c/d15e58cc&sn1=e8e710ce/47158a0f&camp=Cap_One_360_2014_1912371-nyt1&ad=Cap_One_360_HP_Advantage_163x90_010714-DART&goto=http://ad.doubleclick.net/jump/N3282.nytimes.comSD6440/B7976905.2;sz=163x90;pc=nyt234219A361017;ord=2014.02.05.04.43.42?" TARGET="_blank">
<IMG SRC="http://ad.doubleclick.net/ad/N3282.nytimes.comSD6440/B7976905.2;sz=163x90;pc=nyt234219A361017;ord=2014.02.05.04.43.42?"
 BORDER=0 WIDTH=163 HEIGHT=90
 ALT="Click Here"></A></div>
</div>
</div>
</div>
</div>
	</div>


<div class="singleRuleDivider insetH"></div>
<!--Start CColumnAboveMoth region -->
<div class="columnGroup first">				
<div id="classifiedsWidget">
<div id="tabsContainer">
<ul class="tabs">
<li class="" style="border-left:1px solid #CCCCCC"><a href="http://www.nytimes.com/pages/realestate/index.html">Real Estate</a></li>
<li class="selected"><a href="http://www.nytimes.com/autos/">Autos</a></li>
<li class=""><a href="http://jobmarket.nytimes.com/pages/jobs/">Jobs</a></li>
<li class=""><a href="http://www.nytimes.com/ref/classifieds/">All Classifieds</a></li>
</ul> 
</div>
<style type="text/css">
#autos.tabContent{display:block;}

    /* use one of these three
#realEstate.tabContent{display:block;}
#autos.tabContent{display:block;}
#jobMarket.tabContent{display:block;} 

  */
</style>
<div class="tabContent" id="realEstate">
<div class="editColumn">	<h6 class="kicker">Ask Real Estate</h6>
<h5><a href="http://www.nytimes.com/2014/02/02/realestate/why-cant-i-have-a-washing-machine.html?hp">
Why Can’t I Have a Washing Machine?
</a></h5>
<div class="runaroundRight">
<a href="http://www.nytimes.com/2014/02/02/realestate/why-cant-i-have-a-washing-machine.html?hp">
<img src="http://graphics8.nytimes.com/images/2014/02/02/realestate/02ask-image/02ask-image-thumbStandard-v3.jpg" alt="Why Can’t I Have a Washing Machine?" width="75" height="75" />
</a></div>
<p class="summary">
Questions about laundry equipment, an heir’s access to a deceased shareholder’s apartment and who pays for window replacement in a co-op.
</p>
<ul class="refer">
<li><span class="commentCountLink" articleid="http://www.nytimes.com/2014/02/02/realestate/why-cant-i-have-a-washing-machine.html" overflowurl="http://community.nytimes.com/comments/www.nytimes.com/2014/02/02/realestate/why-cant-i-have-a-washing-machine.html?hp&target=comments" articletitle="Why Can't I Have a Washing Machine?"></span>
</li>
</ul>	</div>
<div class="searchColumn">
<h6 class="kicker">Find Properties</h6>
<ul class="refer">
<li><a href="http://www.nytimes.com/pages/realestate/index.html">Go to Real Estate Section</a></li>
<li><a href="http://realestate.nytimes.com/search/advanced.aspx">Search for Properties</a></li>
<li><a href="http://itunes.apple.com/us/app/nytimesrealestate/id337316535?hp">Download the Real Estate App</a></li>
<li><a href="http://www.nytimes.com/pages/realestate/commercial/index.html">Commercial Real Estate</a></li>
<li><a href="http://www.nytimes.com/marketing/realestate/videoshowcase/">Video Showcase: Real Estate</a></li>
<li><a href="http://realestateads.nytimes.com/">Post an Ad</a></li>
</ul>
</div>
<!-- ADXINFO classification="Home_Page_Markets_Module_Tile" campaign="HPModule-CorcSunMH-1911139" priority="8000" isInlineSafe="N" width="163" height="90" --><!--Ad Template Begins Here -->
<div class="story advertisement">
<div class="callout">
<a href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=HPmodule-RE2&sn2=d1cdc681/5274a2cb&sn1=636797db/a6c84b3a&camp=HPModule-CorcSunMH-1911139&ad=MH_Holiday_LivingRoom&goto=http%3A%2F%2Fbs%2Eserving%2Dsys%2Ecom%2FBurstingPipe%2FadServer%2Ebs%3Fcn%3Dtf%26c%3D20%26mc%3Dclick%26pli%3D4608002%26PluID%3D0%26ord%3D%25%25GMTTIME%25%25%20" target="_blank">
<img src="http://graphics8.nytimes.com/adx/images/ADS/35/83/ad.358380/new_living_room_image.jpg" width="173" height="98" border="0" alt="Click for Details"></a>
</div>
<h5>
<a href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=HPmodule-RE2&sn2=d1cdc681/5274a2cb&sn1=636797db/a6c84b3a&camp=HPModule-CorcSunMH-1911139&ad=MH_Holiday_LivingRoom&goto=http%3A%2F%2Fbs%2Eserving%2Dsys%2Ecom%2FBurstingPipe%2FadServer%2Ebs%3Fcn%3Dtf%26c%3D20%26mc%3Dclick%26pli%3D4608002%26PluID%3D0%26ord%3D%25%25GMTTIME%25%25%20" target="_blank"></a>
</h5>
<p class="summary"><a href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=HPmodule-RE2&sn2=d1cdc681/5274a2cb&sn1=636797db/a6c84b3a&camp=HPModule-CorcSunMH-1911139&ad=MH_Holiday_LivingRoom&goto=http%3A%2F%2Fbs%2Eserving%2Dsys%2Ecom%2FBurstingPipe%2FadServer%2Ebs%3Fcn%3Dtf%26c%3D20%26mc%3Dclick%26pli%3D4608002%26PluID%3D0%26ord%3D%25%25GMTTIME%25%25%20" target="_blank">1-4 BDRM Condos<br>Steps from Park Ave.<br>on UES</a>
</p>
<div class="adCreative">
<a href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=HPmodule-RE2&sn2=d1cdc681/5274a2cb&sn1=636797db/a6c84b3a&camp=HPModule-CorcSunMH-1911139&ad=MH_Holiday_LivingRoom&goto=http%3A%2F%2Fbs%2Eserving%2Dsys%2Ecom%2FBurstingPipe%2FadServer%2Ebs%3Fcn%3Dtf%26c%3D20%26mc%3Dclick%26pli%3D4608002%26PluID%3D0%26ord%3D%25%25GMTTIME%25%25%20" target="_blank">
<img src="http://graphics8.nytimes.com/adx/images/ADS/35/83/ad.358380/MH_Logo_Module.gif" width="78" height="36"></a>
</div>
</div>
<!--Ad Template Ends Here -->
<div class="tabFoot story advertisement refer">
<a href="http://listings.nytimes.com/classifiedsmarketplace/?DTab=2&incamp=hpclassifiedsmodule">Place a Classified Ad »</a>
</div>
</div>
<div class="tabContent" id="autos">
<div class="editColumn">	<h6 class="kicker">AUTO EGO</h6>
<h5><a href="http://www.nytimes.com/2014/02/02/automobiles/collectibles/a-hand-me-down-with-a-history.html?hp">
A Hand-Me-Down With a History
</a></h5>
<div class="runaroundRight">
<a href="http://www.nytimes.com/2014/02/02/automobiles/collectibles/a-hand-me-down-with-a-history.html?hp">
<img src="http://graphics8.nytimes.com/images/2014/02/02/automobiles/EGO1/EGO1-thumbStandard-v2.jpg" alt="A Hand-Me-Down With a History" width="75" height="75" />
</a></div>
<p class="summary">
Randy Mehrberg’s 1952 MG TD was a gift from his uncle Morty, who taught Randy to drive in the MG decades ago.
</p>
<ul class="refer">
<a href="http://www.nytimes.com/slideshow/2014/02/02/automobiles/collectibles/02ego-slides.html?hp"><span class="icon slideshow">Slide Show</span>: Keeping It in the Family</a>
</ul>	</div>
<div class="searchColumn"><style type="text/css">
      #searchUsedCompact select,
      #searchNewCompact select {
        width:106px;
        vertical-align:top;
        font-family: Arial, Helvetica, sans-serif;
        font-size:11px;
        color:#333;
      }

    #searchUsedCompact .gabrielsImageButton,
    #searchNewCompact .gabrielsImageButton {
    vertical-align:top;
    }
  
    #classifiedsWidget .autosStory,
    #classifiedsWidget .autosStory {
    vertical-align:top;
    border-bottom:1px solid #ccc;
    padding:0 0 7px;
    margin:0 0 7px !important;
    }
  
    #classifiedsWidget #zipCode {
    width:99px;
    height:15px;
    }

    #makesUsed {
    margin-bottom:5px;
    }
    </style><script type="text/javascript">
      AutosSearch = {};
      AutosSearch.setNameFromSelect = function(el,select) {
        document.getElementById(el).value = select.options[select.selectedIndex].text;
      }
    </script><div class="story autosStory"><h6 class="kicker">New Cars Search</h6><form method="post" action="http://autos.nytimes.com/researchSelect.aspx" id="searchNewCompact"><select id="makesNew" name="makes" onchange="AutosSearch.setNameFromSelect('makeNamesNew',this)"><option value="0">Select Make </option><option value="227">Acura</option><option value="231">Aston Martin</option><option value="232">Audi</option><option value="233">Bentley</option><option value="235">BMW</option><option value="236">Buick</option><option value="237">Cadillac</option><option value="238">Chevrolet</option><option value="239">Chrysler</option><option value="242">Dodge</option><option value="244">Ferrari</option><option value="245">Ford</option><option value="247">GMC</option><option value="248">Honda</option><option value="249">Hummer</option><option value="250">Hyundai</option><option value="251">Infiniti</option><option value="252">Isuzu</option><option value="253">Jaguar</option><option value="254">Jeep</option><option value="255">Kia</option><option value="256">Lamborghini</option><option value="257">Land Rover</option><option value="258">Lexus</option><option value="259">Lincoln</option><option value="261">Maserati</option><option value="262">Maybach</option><option value="263">Mazda</option><option value="264">Mercedes-Benz</option><option value="265">Mercury</option><option value="267">MINI</option><option value="268">Mitsubishi</option><option value="269">Nissan</option><option value="270">Oldsmobile</option><option value="272">Panoz</option><option value="275">Plymouth</option><option value="276">Pontiac</option><option value="277">Porsche</option><option value="280">Saab</option><option value="281">Saturn</option><option value="282">Scion</option><option value="284">Subaru</option><option value="285">Suzuki</option><option value="286">Toyota</option><option value="287">Volkswagen</option><option value="288">Volvo</option><option value="290">MG</option><option value="291">Rolls-Royce</option><option value="999">Other</option></select><input type="hidden" name="makeNames" id="makeNamesNew" value="" /> <input class="gabrielsImageButton" alt="Go" type="image" src="http://graphics8.nytimes.com/images/global/buttons/go.gif"></form></div><div class="story autosStory"><h6 class="kicker">Used Cars Search</h6><form method="post" action="http://autos.nytimes.com/search.aspx" id="searchUsedCompact"><select id="makesUsed" name="makeId" onchange="AutosSearch.setNameFromSelect('makeNamesUsed',this)"><option value="0">Select Make </option><option value="227">Acura</option><option value="231">Aston Martin</option><option value="232">Audi</option><option value="233">Bentley</option><option value="235">BMW</option><option value="236">Buick</option><option value="237">Cadillac</option><option value="238">Chevrolet</option><option value="239">Chrysler</option><option value="242">Dodge</option><option value="244">Ferrari</option><option value="245">Ford</option><option value="247">GMC</option><option value="248">Honda</option><option value="249">Hummer</option><option value="250">Hyundai</option><option value="251">Infiniti</option><option value="252">Isuzu</option><option value="253">Jaguar</option><option value="254">Jeep</option><option value="255">Kia</option><option value="256">Lamborghini</option><option value="257">Land Rover</option><option value="258">Lexus</option><option value="259">Lincoln</option><option value="261">Maserati</option><option value="262">Maybach</option><option value="263">Mazda</option><option value="264">Mercedes-Benz</option><option value="265">Mercury</option><option value="267">MINI</option><option value="268">Mitsubishi</option><option value="269">Nissan</option><option value="270">Oldsmobile</option><option value="272">Panoz</option><option value="275">Plymouth</option><option value="276">Pontiac</option><option value="277">Porsche</option><option value="280">Saab</option><option value="281">Saturn</option><option value="282">Scion</option><option value="284">Subaru</option><option value="285">Suzuki</option><option value="286">Toyota</option><option value="287">Volkswagen</option><option value="288">Volvo</option><option value="290">MG</option><option value="291">Rolls-Royce</option><option value="999">Other</option></select><br>
<input type="hidden" name="makeNames" id="makeNamesUsed" value="" />
<input type="text" name="zipCode" id="zipCode" value="Enter ZIP code"
  onfocus="if(this.value=='Enter ZIP code') { this.value=''; }"
  onblur="if(this.value==null || this.value=='') { this.value='Enter ZIP code'; }"> <input class="gabrielsImageButton" alt="Go" type="image" src="http://graphics8.nytimes.com/images/global/buttons/go.gif"></form></div><h6 class="kicker">More in Automobiles</h6><ul class="refer"><li><a href="http://www.nytimes.com/pages/automobiles/reviews/index.html">New Car Reviews</a></li><li><a href="http://autos.nytimes.com/used.aspx">Used Car Information</a></li><li><a href="http://www.nytimes.com/pages/automobiles/collectiblecars/index.html">Collectible Cars</a></li><li><a href="https://placead.nytimes.com/default.asp?CategoryID=NYTCAR">Sell Your Car</a></li></ul>
</div>
<!-- ADXINFO classification="Home_Page_Markets_Module_Tile" campaign="HPModule-CorcSunMH-1911139" priority="8000" isInlineSafe="N" width="163" height="90" --><!--Ad Template Begins Here -->
<div class="story advertisement">
<div class="callout">
<a href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=HPmodule-RE2&sn2=d1cdc681/5274a2cb&sn1=636797db/a6c84b3a&camp=HPModule-CorcSunMH-1911139&ad=MH_Holiday_LivingRoom&goto=http%3A%2F%2Fbs%2Eserving%2Dsys%2Ecom%2FBurstingPipe%2FadServer%2Ebs%3Fcn%3Dtf%26c%3D20%26mc%3Dclick%26pli%3D4608002%26PluID%3D0%26ord%3D%25%25GMTTIME%25%25%20" target="_blank">
<img src="http://graphics8.nytimes.com/adx/images/ADS/35/83/ad.358380/new_living_room_image.jpg" width="173" height="98" border="0" alt="Click for Details"></a>
</div>
<h5>
<a href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=HPmodule-RE2&sn2=d1cdc681/5274a2cb&sn1=636797db/a6c84b3a&camp=HPModule-CorcSunMH-1911139&ad=MH_Holiday_LivingRoom&goto=http%3A%2F%2Fbs%2Eserving%2Dsys%2Ecom%2FBurstingPipe%2FadServer%2Ebs%3Fcn%3Dtf%26c%3D20%26mc%3Dclick%26pli%3D4608002%26PluID%3D0%26ord%3D%25%25GMTTIME%25%25%20" target="_blank"></a>
</h5>
<p class="summary"><a href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=HPmodule-RE2&sn2=d1cdc681/5274a2cb&sn1=636797db/a6c84b3a&camp=HPModule-CorcSunMH-1911139&ad=MH_Holiday_LivingRoom&goto=http%3A%2F%2Fbs%2Eserving%2Dsys%2Ecom%2FBurstingPipe%2FadServer%2Ebs%3Fcn%3Dtf%26c%3D20%26mc%3Dclick%26pli%3D4608002%26PluID%3D0%26ord%3D%25%25GMTTIME%25%25%20" target="_blank">1-4 BDRM Condos<br>Steps from Park Ave.<br>on UES</a>
</p>
<div class="adCreative">
<a href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=HPmodule-RE2&sn2=d1cdc681/5274a2cb&sn1=636797db/a6c84b3a&camp=HPModule-CorcSunMH-1911139&ad=MH_Holiday_LivingRoom&goto=http%3A%2F%2Fbs%2Eserving%2Dsys%2Ecom%2FBurstingPipe%2FadServer%2Ebs%3Fcn%3Dtf%26c%3D20%26mc%3Dclick%26pli%3D4608002%26PluID%3D0%26ord%3D%25%25GMTTIME%25%25%20" target="_blank">
<img src="http://graphics8.nytimes.com/adx/images/ADS/35/83/ad.358380/MH_Logo_Module.gif" width="78" height="36"></a>
</div>
</div>
<!--Ad Template Ends Here -->
<div class="tabFoot story advertisement refer"><a href="http://listings.nytimes.com/classifiedsmarketplace/?DTab=2&incamp=hpclassifiedsmodule">Place a Classified Ad »</a></div>
</div>
<div class="tabContent" id="jobMarket">
<h3 class="sectionHeader"><a href="http://www.nytimes.com/monster"><img src="http://graphics8.nytimes.com/images/section/jobs/200703/cobrandHeader_315x20.gif" width="315" height="20" alt="NYTimes.com / Monster" /></a></h3>
<div class="editColumn">	<h6 class="kicker">Corner Office</h6>
<h5><a href="http://www.nytimes.com/2013/12/29/business/carey-smith-on-becoming-the-teams-hyperlink.html">
Carey Smith, on Becoming the Team’s ‘Hyperlink’
</a></h5>
<div class="runaroundRight">
<a href="http://www.nytimes.com/2013/12/29/business/carey-smith-on-becoming-the-teams-hyperlink.html">
<img src="http://graphics8.nytimes.com/images/2013/12/26/business/26-CORNER/26-CORNER-thumbStandard-v2.jpg" alt="
Carey Smith, on Becoming the Team’s ‘Hyperlink’" width="75" height="75" />
</a></div>
<p class="summary">
“I have an office, but most of the time I just walk around and try to determine if we’ve got any problems.” 
</p>	</div>
<div class="searchColumn">
<p style="font:bold 1.1em Arial; margin:0 0 10px 0">Find the best job in the New York metro area and beyond.</p>
<form class="searchForm" action="http://nytimes.monster.com/Search.aspx" method="get" name="advJobsearchForm">
<input type="hidden" name="cy" value="us" />
<input id="searchQuery" name="q" value="" />    
<input id="searchSubmit" title="Search" alt="Search" type="image" src="http://graphics8.nytimes.com/images/global/global_search/search_button40x19.gif">  <a class="refer" href="http://jobmarket.nytimes.com/jobs/search-jobs/">Advanced Search »</a> 
</form>
</div>
<div class="toolsCol">
<h6 class="kicker">Tools</h6>
<ul class="refer">
<li><a href="http://www.nytimes.com/marketing/jobmarket/postresume.html">Post Your Resumé to NYTimes.com/monster</a></li>
<li><a href="http://jobmarket.nytimes.com/jobs/category/">Find a Job by Industry</a></li>
</ul>
</div>
<div class="employersCol">
<h6 class="kicker">Employers</h6>
<ul class="refer">
<li style="width: 177px;"><a href="http://www.nytimes.com/marketing/jobmarket/employercentral/postjob.html">Post a Job Online and in Print</a></li>
<li><a href="http://hiring.nytimes.monster.com/products/resumeproducts.aspx">Search Résumés</a></li>
<li><a href="http://www.nytimes.com/marketing/jobmarket/employercentral/index.html">See All Recruitment Options</a></li>
</ul>
</div>
<!-- ADXINFO classification="Home_Page_Markets_Module_Tile" campaign="HPModule-CorcSunMH-1911139" priority="8000" isInlineSafe="N" width="163" height="90" --><!--Ad Template Begins Here -->
<div class="story advertisement">
<div class="callout">
<a href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=HPmodule-RE2&sn2=d1cdc681/5274a2cb&sn1=636797db/a6c84b3a&camp=HPModule-CorcSunMH-1911139&ad=MH_Holiday_LivingRoom&goto=http%3A%2F%2Fbs%2Eserving%2Dsys%2Ecom%2FBurstingPipe%2FadServer%2Ebs%3Fcn%3Dtf%26c%3D20%26mc%3Dclick%26pli%3D4608002%26PluID%3D0%26ord%3D%25%25GMTTIME%25%25%20" target="_blank">
<img src="http://graphics8.nytimes.com/adx/images/ADS/35/83/ad.358380/new_living_room_image.jpg" width="173" height="98" border="0" alt="Click for Details"></a>
</div>
<h5>
<a href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=HPmodule-RE2&sn2=d1cdc681/5274a2cb&sn1=636797db/a6c84b3a&camp=HPModule-CorcSunMH-1911139&ad=MH_Holiday_LivingRoom&goto=http%3A%2F%2Fbs%2Eserving%2Dsys%2Ecom%2FBurstingPipe%2FadServer%2Ebs%3Fcn%3Dtf%26c%3D20%26mc%3Dclick%26pli%3D4608002%26PluID%3D0%26ord%3D%25%25GMTTIME%25%25%20" target="_blank"></a>
</h5>
<p class="summary"><a href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=HPmodule-RE2&sn2=d1cdc681/5274a2cb&sn1=636797db/a6c84b3a&camp=HPModule-CorcSunMH-1911139&ad=MH_Holiday_LivingRoom&goto=http%3A%2F%2Fbs%2Eserving%2Dsys%2Ecom%2FBurstingPipe%2FadServer%2Ebs%3Fcn%3Dtf%26c%3D20%26mc%3Dclick%26pli%3D4608002%26PluID%3D0%26ord%3D%25%25GMTTIME%25%25%20" target="_blank">1-4 BDRM Condos<br>Steps from Park Ave.<br>on UES</a>
</p>
<div class="adCreative">
<a href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=HPmodule-RE2&sn2=d1cdc681/5274a2cb&sn1=636797db/a6c84b3a&camp=HPModule-CorcSunMH-1911139&ad=MH_Holiday_LivingRoom&goto=http%3A%2F%2Fbs%2Eserving%2Dsys%2Ecom%2FBurstingPipe%2FadServer%2Ebs%3Fcn%3Dtf%26c%3D20%26mc%3Dclick%26pli%3D4608002%26PluID%3D0%26ord%3D%25%25GMTTIME%25%25%20" target="_blank">
<img src="http://graphics8.nytimes.com/adx/images/ADS/35/83/ad.358380/MH_Logo_Module.gif" width="78" height="36"></a>
</div>
</div>
<!--Ad Template Ends Here -->
<div class="tabFoot story advertisement refer"><a href="http://listings.nytimes.com/classifiedsmarketplace/?DTab=2&incamp=hpclassifiedsmodule">Place a Classified Ad »</a></div>
</div>
<style type="text/css" media="screen">
#classifiedsWidget .tabContent .subColumns{background:transparent;}
#classifiedsWidget .tabContent .subColumnA li,#classifiedsWidget .tabContent .subColumnB li{font-size:1.1em;}
</style>
<div class="tabContent" id="allClassifieds">
<h6 class="kicker">Find a Classifieds Listing</h6>
<div class="subColumns">
<div class="subColumnA">
<ul>
<li><a href="http://www.nytimes.com/autos/">Autos</a></li>
<li><a href="http://listings.nytimes.com/BusinessDirectory/searchindex.asp">Business Directory</a></li>
<li><a href="http://listings.nytimes.com/campsandschools/searchindex.asp">Camps & Schools</a></li>
<li><a href="http://www.nytimes.com/pages/realestate/commercial/">Commercial Real Estate</a></li>
<li><a href="http://listings.nytimes.com/HomeandGarden/searchindex.asp">Home & Garden Directory</a></li>
<li><a href="http://jobmarket.nytimes.com/pages/jobs/">Jobs</a></li>
</ul>
</div>
<div class="subColumnB">
<ul>
<!--<li><a href="http://query.nytimes.com/gst/personals.html">Personals</a></li>
-->
<li><a href="http://www.legacy.com/nytimes/celebrations.asp?Page=SearchResults">Social Announcements</a></li>
<li><a href="http://www.nytimes.com/pages/realestate/">Residental Real Estate</a></li>
<li><a href="http://listings.nytimes.com/SmallInnsAndLodges/searchindex.asp">Small Inns & Lodges</a></li>
<li><a href="http://listings.nytimes.com/Weddings/searchindex.asp">Weddings Directory</a></li>
</ul>
</div>
</div>
<ul class="refer">
<li><a href="http://listings.nytimes.com/ClassifiedsMarketplace/default.asp?DTab=2">Post a Classified Ad Online</a> | <a href="http://www.nytadvertising.com/was/ATWWeb/public/index.jsp">In Print</a></li>
</ul>
<div class="tabFoot story advertisement refer"><a href="http://listings.nytimes.com/classifiedsmarketplace/?DTab=2&incamp=hpclassifiedsmodule">Place a Classified Ad »</a></div>
</div></div>
<!--close allClassifieds -->
<script type="text/javascript">new Accordian("classifiedsWidget");</script>



<div class="singleAd" id="HPMiddle3">
<!-- ADXINFO classification="Marketing_300x79" campaign="nyt2013_300x79_HP_corneroffice" priority="1000" isInlineSafe="N" width="300" height="79" --><div align="center"><a href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=HPMiddle3&sn2=2798b754/f0b6765&sn1=9264695a/7eec88b6&camp=nyt2013_300x79_HP_corneroffice&ad=300x79_corneroffice&goto=http%3A%2F%2Fprojects%2Enytimes%2Ecom%2Fcorner%2Doffice" target="_blank">
<img src="http://graphics8.nytimes.com/adx/images/ADS/35/95/ad.359513/13-1919_CornerOfficeBanner_300x79_DM.jpg" width="300" height="79" border="0">
</a></div>
</div>



<script type="text/javascript">
/* Generated at 2013-10-29T02:31:41-04:00 */
renditionMapping = {"images/2013/10/29/world/PREXY/PREXY-hpSmall.jpg":{"path":"images/2013/10/29/world/PREXY/PREXY-mediumFlexible177.jpg","w":"177","h":"113"},"images/2013/10/29/world/PREXY/PREXY-hpMedium-v2.jpg":{"path":"images/2013/10/29/world/PREXY/PREXY-largeHorizontal375.jpg","w":"375","h":"250"},"images/2013/10/29/world/PREXY/PREXY-hpLarge.jpg":{"path":"images/2013/10/29/world/PREXY/PREXY-largeWidescreen573.jpg","w":"573","h":"287"},"images/2013/10/29/us/29ABORTION/29ABORTION-hpSmall.jpg":{"path":"images/2013/10/29/us/29ABORTION/29ABORTION-mediumFlexible177.jpg","w":"177","h":"120"},"images/2013/10/29/us/29ABORTION/29ABORTION-hpMedium.jpg":{"path":"images/2013/10/29/us/29ABORTION/29ABORTION-largeHorizontal375.jpg","w":"375","h":"250"},"images/2013/10/29/us/29ABORTION/29ABORTION-hpLarge.jpg":{"path":"images/2013/10/29/us/29ABORTION/29ABORTION-largeWidescreen573.jpg","w":"573","h":"287"},"images/2013/10/29/us/TAVENNER/TAVENNER-hpSmall.jpg":{"path":"images/2013/10/29/us/TAVENNER/TAVENNER-mediumFlexible177.jpg","w":"177","h":"110"},"images/2013/10/29/us/TAVENNER/TAVENNER-hpMedium-v2.jpg":{"path":"images/2013/10/29/us/TAVENNER/TAVENNER-largeHorizontal375.jpg","w":"375","h":"250"},"images/2013/10/29/us/TAVENNER/TAVENNER-hpLarge.jpg":{"path":"images/2013/10/29/us/TAVENNER/TAVENNER-largeWidescreen573.jpg","w":"573","h":"287"},"images/2013/10/29/sports/SERIES1/SERIES1-hpSmall.jpg":{"path":"images/2013/10/29/sports/SERIES1/SERIES1-mediumFlexible177.jpg","w":"177","h":"124"},"images/2013/10/29/sports/SERIES1/SERIES1-hpMedium.jpg":{"path":"images/2013/10/29/sports/SERIES1/SERIES1-largeHorizontal375.jpg","w":"375","h":"250"},"images/2013/10/29/sports/SERIES1/SERIES1-hpLarge.jpg":{"path":"images/2013/10/29/sports/SERIES1/SERIES1-largeWidescreen573.jpg","w":"573","h":"287"},"images/2013/10/29/us/DETROIT/DETROIT-hpSmall.jpg":{"path":"images/2013/10/29/us/DETROIT/DETROIT-mediumFlexible177.jpg","w":"177","h":"118"},"images/2013/10/29/us/DETROIT/DETROIT-hpMedium-v2.jpg":{"path":"images/2013/10/29/us/DETROIT/DETROIT-largeHorizontal375.jpg","w":"375","h":"250"},"images/2013/10/29/us/DETROIT/DETROIT-hpLarge-v2.jpg":{"path":"images/2013/10/29/us/DETROIT/DETROIT-largeWidescreen573-v2.jpg","w":"573","h":"287"},"images/2013/10/29/business/Schools1/Schools1-hpSmall.jpg":{"path":"images/2013/10/29/business/Schools1/Schools1-mediumFlexible177.jpg","w":"177","h":"118"},"images/2013/10/29/business/Schools1/Schools1-hpMedium.jpg":{"path":"images/2013/10/29/business/Schools1/Schools1-largeHorizontal375.jpg","w":"375","h":"250"},"images/2013/10/29/business/Schools1/Schools1-hpLarge.jpg":{"path":"images/2013/10/29/business/Schools1/Schools1-largeWidescreen573.jpg","w":"573","h":"287"},"images/2013/10/29/us/SKELTON-obit/SKELTON-obit-hpSmall.jpg":{"path":"images/2013/10/29/us/SKELTON-obit/SKELTON-obit-mediumFlexible177.jpg","w":"177","h":"221"},"images/2013/10/29/us/SKELTON-obit/SKELTON-obit-hpMedium.jpg":{"path":"images/2013/10/29/us/SKELTON-obit/SKELTON-obit-largeHorizontal375.jpg","w":"375","h":"250"},"images/2013/10/29/us/SKELTON-obit/SKELTON-obit-hpLarge.jpg":{"path":"images/2013/10/29/us/SKELTON-obit/SKELTON-obit-largeWidescreen573.jpg","w":"573","h":"286"},"images/2013/10/29/sports/SANDUSKY/SANDUSKY-hpSmall.jpg":{"path":"images/2013/10/29/sports/SANDUSKY/SANDUSKY-mediumFlexible177.jpg","w":"177","h":"118"},"images/2013/10/29/sports/SANDUSKY/SANDUSKY-hpMedium-v2.jpg":{"path":"images/2013/10/29/sports/SANDUSKY/SANDUSKY-largeHorizontal375-v2.jpg","w":"375","h":"250"},"images/2013/10/29/sports/SANDUSKY/SANDUSKY-hpLarge-v2.jpg":{"path":"images/2013/10/29/sports/SANDUSKY/SANDUSKY-largeWidescreen573-v2.jpg","w":"573","h":"287"},"images/2013/10/29/nyregion/ELLIS1/ELLIS1-hpSmall.jpg":{"path":"images/2013/10/29/nyregion/ELLIS1/ELLIS1-mediumFlexible177.jpg","w":"177","h":"139"},"images/2013/10/29/nyregion/ELLIS1/ELLIS1-hpMedium.jpg":{"path":"images/2013/10/29/nyregion/ELLIS1/ELLIS1-largeHorizontal375.jpg","w":"375","h":"250"},"images/2013/10/29/nyregion/ELLIS1/ELLIS1-hpLarge.jpg":{"path":"images/2013/10/29/nyregion/ELLIS1/ELLIS1-largeWidescreen573.jpg","w":"573","h":"287"},"images/2013/10/29/nyregion/y-banksy1/y-banksy1-hpSmall.jpg":{"path":"images/2013/10/29/nyregion/y-banksy1/y-banksy1-mediumFlexible177.jpg","w":"177","h":"118"},"images/2013/10/29/nyregion/y-banksy1/y-banksy1-hpMedium-v2.jpg":{"path":"images/2013/10/29/nyregion/y-banksy1/y-banksy1-largeHorizontal375.jpg","w":"375","h":"250"},"images/2013/10/29/nyregion/y-banksy1/y-banksy1-hpLarge.jpg":{"path":"images/2013/10/29/nyregion/y-banksy1/y-banksy1-largeWidescreen573.jpg","w":"573","h":"286"}};
</script>	</div>
<!--End CColumnAboveMoth region -->
<!--Start CColumnAboveMothBottom -->
<div class="columnGroup">
</div><!--end .columnGroup -->
<!--End CColumnAboveMothBottom -->


</div>
</div><!--close cColumn -->
</div><!--close spanAB -->
</div><!--close column -->
</div><!--close baseLayout -->
<!--start MOTH -->
<div id="insideNYTimes" class="doubleRule nocontent">
<div id="insideNYTimesHeader">
<div class="navigation"><span id="leftArrow"><img id="mothReverse" src="http://i1.nyt.com/images/global/buttons/moth_reverse.gif" /></span>&nbsp;<span id="rightArrow"><img id="mothForward" src="http://i1.nyt.com/images/global/buttons/moth_forward.gif" /></span></div>
<h4>
Inside NYTimes.com        </h4>
</div>
<div id="insideNYTimesScrollWrapper">
<table id="insideNYTimesBrowser" cellspacing="0">
<tbody>
<tr>
<td class="first">
<div class="story">
<h6 class="kicker">
<a href="http://www.nytimes.com/pages/theater/index.html">Theater »</a>                            </h6>
<div class="mothImage">
<a href="http://www.nytimes.com/2014/02/04/theater/carly-rae-jepsen-to-star-as-cinderella.html"><img src="http://i1.nyt.com/images/2014/02/04/theater/04moth_jepsen/04moth_jepsen-moth.jpg" alt="Carly Rae Jepsen Takes a &lsquo;Cinderella&rsquo; Risk" width="151" height="151" /></a>
</div>
<h6 class="headline"><a href="http://www.nytimes.com/2014/02/04/theater/carly-rae-jepsen-to-star-as-cinderella.html">Carly Rae Jepsen Takes a &lsquo;Cinderella&rsquo; Risk</a></h6>
</div>
</td>
<td>
<div class="story">
<h6 class="kicker">
<a href="http://www.nytimes.com/pages/books/index.html">Books »</a>                            </h6>
<div class="mothImage">
<a href="http://www.nytimes.com/2014/02/04/books/an-officer-and-a-spy-is-robert-harriss-latest-novel.html"><img src="http://i1.nyt.com/images/2014/02/04/books/04moth_bookharris/04moth_bookharris-moth.jpg" alt="For a Frenchman, Pursuit Was Real" width="151" height="151" /></a>
</div>
<h6 class="headline"><a href="http://www.nytimes.com/2014/02/04/books/an-officer-and-a-spy-is-robert-harriss-latest-novel.html">For a Frenchman, Pursuit Was Real</a></h6>
</div>
</td>
<td>
<div class="story">
<h6 class="kicker"><a href="http://www.nytimes.com/pages/opinion/index.html">Opinion »</a></h6>
<h3><a href="http://www.nytimes.com/2014/02/04/opinion/dont-let-putin-grab-ukraine.html">Op-Ed: Don&rsquo;t Let Putin Grab Ukraine</a></h3>
<p class="summary">Russia’s dream of a Eurasian Union, with a puppet regime in Ukraine, will lead to more violence.</p>
</div>
</td>
<td>
<div class="story">
<h6 class="kicker">
<a href="http://www.nytimes.com/pages/national/index.html">U.S. »</a>                            </h6>
<div class="mothImage">
<a href="http://www.nytimes.com/2014/02/04/us/while-asking-for-help-detroit-sells-a-comeback.html"><img src="http://i1.nyt.com/images/2014/02/04/us/04moth_image/04moth_image-moth.jpg" alt="While Asking for Help, Detroit Sells a Comeback" width="151" height="151" /></a>
</div>
<h6 class="headline"><a href="http://www.nytimes.com/2014/02/04/us/while-asking-for-help-detroit-sells-a-comeback.html">While Asking for Help, Detroit Sells a Comeback</a></h6>
</div>
</td>
<td>
<div class="story">
<h6 class="kicker"><a href="http://www.nytimes.com/pages/opinion/index.html">Opinion »</a></h6>
<h3><a href="http://www.nytimes.com/2014/02/04/opinion/a-chill-on-speech.html">Editorial: A Chill on Speech</a></h3>
<p class="summary">A New York State bill in response to a resolution to boycott Israeli academic institutions would trample on academic freedoms and free speech.</p>
</div>
</td>
<td>
<div class="story">
<h6 class="kicker">
<a href="http://www.nytimes.com/pages/science/index.html">Science »</a>                            </h6>
<div class="mothImage">
<a href="http://www.nytimes.com/2014/02/04/science/to-study-aggression-a-fight-club-for-flies.html"><img src="http://i1.nyt.com/images/2014/02/04/science/04MOTH_FLY/04MOTH_FLY-moth.jpg" alt="A Fight Club for Flies" width="151" height="151" /></a>
</div>
<h6 class="headline"><a href="http://www.nytimes.com/2014/02/04/science/to-study-aggression-a-fight-club-for-flies.html">A Fight Club for Flies</a></h6>
</div>
</td>
<td class="hidden">
<div class="story">
<h6 class="kicker">
<a href="http://www.nytimes.com/pages/business/index.html">Business Day »</a>                            </h6>
<div class="mothImage">
<a href="http://www.nytimes.com/2014/02/04/technology/fast-internet-service-speeds-business-development-in-chattanooga.html"><span class="img" src="http://i1.nyt.com/images/2014/02/04/business/04moth_chattanooga/04moth_chattanooga-moth.jpg" alt="Chattanooga, a City Wired for Growth" width="151" height="151" /></a>
</div>
<h6 class="headline"><a href="http://www.nytimes.com/2014/02/04/technology/fast-internet-service-speeds-business-development-in-chattanooga.html">Chattanooga, a City Wired for Growth</a></h6>
</div>
</td>
<td class="hidden">
<div class="story">
<h6 class="kicker">
<a href="http://www.nytimes.com/pages/nyregion/index.html">N.Y./Region »</a>                            </h6>
<div class="mothImage">
<a href="http://www.nytimes.com/2014/02/04/nyregion/de-blasio-takes-a-comedic-break-on-the-daily-show.html"><span class="img" src="http://i1.nyt.com/images/2014/02/04/nyregion/04moth_dailyshow/04moth_dailyshow-moth.jpg" alt="De Blasio Takes On &lsquo;The Daily Show&rsquo;" width="151" height="151" /></a>
</div>
<h6 class="headline"><a href="http://www.nytimes.com/2014/02/04/nyregion/de-blasio-takes-a-comedic-break-on-the-daily-show.html">De Blasio Takes On &lsquo;The Daily Show&rsquo;</a></h6>
</div>
</td>
<td class="hidden">
<div class="story">
<h6 class="kicker">
<a href="http://www.nytimes.com/pages/health/index.html">Health »</a>                            </h6>
<div class="mothImage">
<a href="http://well.blogs.nytimes.com/2014/02/03/weighing-testosterone-benefits-and-risks/"><span class="img" src="http://i1.nyt.com/images/2014/02/04/science/04MOTH_CONS/04MOTH_CONS-moth.jpg" alt="Weighing Testosterone&rsquo;s Benefits and Risks" width="151" height="151" /></a>
</div>
<h6 class="headline"><a href="http://well.blogs.nytimes.com/2014/02/03/weighing-testosterone-benefits-and-risks/">Weighing Testosterone&rsquo;s Benefits and Risks</a></h6>
</div>
</td>
<td class="hidden">
<div class="story">
<h6 class="kicker">
<a href="http://www.nytimes.com/pages/opinion/index.html">Opinion »</a>                            </h6>
<div class="mothImage">
<a href="http://www.nytimes.com/roomfordebate/2014/02/03/the-casual-couture-of-the-average-american/?ref=opinion"><span class="img" src="http://i1.nyt.com/images/2014/02/04/opinion/04moth_rfd/04moth_rfd-moth.jpg" alt="Room for Debate: Is It Pass&eacute; to Dress Nicely?" width="151" height="151" /></a>
</div>
<h6 class="headline"><a href="http://www.nytimes.com/roomfordebate/2014/02/03/the-casual-couture-of-the-average-american/?ref=opinion">Room for Debate: Is It Pass&eacute; to Dress Nicely?</a></h6>
</div>
</td>
<td class="hidden">
<div class="story">
<h6 class="kicker"><a href="http://www.nytimes.com/pages/opinion/index.html">Opinion »</a></h6>
<h3><a href="http://opinionator.blogs.nytimes.com/2014/02/03/dissecting-a-frog-how-to-write-a-humor-piece/">Teddy Wayne: How to Write a Humor Piece</a></h3>
<p class="summary">Writing comedy is a highly logical exercise — fit idea X into form Y for humorous result Z.</p>
</div>
</td>
<td class="hidden">
<div class="story">
<h6 class="kicker">
<a href="http://topics.nytimes.com/top/features/timestopics/series/booming/index.html">Booming »</a>                            </h6>
<div class="mothImage">
<a href="http://www.nytimes.com/2014/02/04/booming/stevie-nicks-just-following-her-muse.html"><span class="img" src="http://i1.nyt.com/images/2014/01/30/booming/04moth-booming-nicks/04moth-booming-nicks-moth-v2.jpg" alt="Stevie Nicks, Just Following Her Muse" width="151" height="151" /></a>
</div>
<h6 class="headline"><a href="http://www.nytimes.com/2014/02/04/booming/stevie-nicks-just-following-her-muse.html">Stevie Nicks, Just Following Her Muse</a></h6>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div><!--end #insideNYTimes -->
<!--end MOTH -->
<div class="baseLayoutBelowFold wrap spanABWell">
<div class="doubleRule">
<div class="column last">
<div class="spanABBelowFold wrap">
<div class="abColumn">
<div id="wellRegion"><div class="module wrap"><div class="column firstColumn"><h6 class="moduleHeaderLg"><a href="http://www.nytimes.com/pages/world/index.html">World  &raquo;</a></h6><ul class="headlinesOnly"><li class="firstItem wrap"><a class="thumb runaroundRight" href="http://www.nytimes.com/2014/02/05/world/middleeast/pakistani-side-fails-to-show-up-at-taliban-peace-talks.html?hpw&rref=world"><img src="http://graphics8.nytimes.com/images/2014/02/05/world/PAKISTAN/PAKISTAN-thumbStandard.jpg" /></a><h6><a href="http://www.nytimes.com/2014/02/05/world/middleeast/pakistani-side-fails-to-show-up-at-taliban-peace-talks.html?hpw&rref=world">Pakistani Side Fails to Show Up at Taliban Peace Talks</a></h6></li><li class=""><h6><a  href="http://www.nytimes.com/2014/02/05/world/asia/philippine-leader-urges-international-help-in-resisting-chinas-sea-claims.html?hpw&rref=world">Philippine Leader Sounds Alarm on China</a></h6></li><li class="lastItem"><h6><a  href="http://www.nytimes.com/2014/02/05/world/europe/russia-blocks-several-activists-from-olympics-even-as-spectators.html?hpw&rref=world">Russia Blocks Several Activists From Olympics, Even as Spectators</a></h6></li></ul></div><div class="column"><h6 class="moduleHeaderLg"><a href="http://www.nytimes.com/pages/business/index.html">Business Day &raquo;</a></h6><ul class="headlinesOnly"><li class="firstItem wrap"><a class="thumb runaroundRight" href="http://www.nytimes.com/2014/02/05/technology/new-boss-at-microsoft-with-gates-at-his-side.html?hpw&rref=business"><img src="http://graphics8.nytimes.com/images/2014/02/05/business/MICROSOFT/MICROSOFT-thumbStandard.jpg" /></a><h6><a href="http://www.nytimes.com/2014/02/05/technology/new-boss-at-microsoft-with-gates-at-his-side.html?hpw&rref=business">New Boss at Microsoft, With Gates at His Side</a></h6></li><li class=""><h6><a  href="http://www.nytimes.com/2014/02/05/business/wellpoint-a-onetime-critic-of-health-law-may-yet-profit.html?hpw&rref=business">WellPoint, a Onetime Critic of Health Law, May Yet Profit</a></h6></li><li class="lastItem"><h6><a  href="http://www.nytimes.com/2014/02/05/business/economy/lenders-see-write-off-while-underwater-homeowners-face-stiff-taxes.html?hpw&rref=business">Welcome Relief for Homeowners, Then the Tax Bill</a></h6></li></ul></div><div class="column lastColumn"><h6 class="moduleHeaderLg"><a href="http://www.nytimes.com/pages/opinion/index.html">Opinion &raquo;</a></h6><ul class="headlinesOnly"><li class="firstItem wrap"><a class="thumb runaroundRight" href="http://www.nytimes.com/2014/02/05/opinion/yu-hua-chinas-censorship-pendulum.html?hpw&rref=opinion"><img src="http://graphics8.nytimes.com/images/2014/02/04/opinion/04yu/04yu-thumbStandard.jpg" /></a><h6><a href="http://www.nytimes.com/2014/02/05/opinion/yu-hua-chinas-censorship-pendulum.html?hpw&rref=opinion">Op-Ed | Yu Hua: The Censorship Pendulum</a></h6></li><li class=""><h6><a  href="http://www.nytimes.com/2014/02/05/opinion/freeing-workers-from-the-insurance-trap.html?hpw&rref=opinion">Today&#039;s Editorials: Freeing Workers From the Insurance Trap</a></h6></li><li class="lastItem"><h6><a  href="http://www.nytimes.com/2014/02/05/opinion/dowd-high-school-maniacal.html?hpw&rref=opinion">Op-Ed Columnist: High School Maniacal</a></h6></li></ul></div></div><div class="module wrap"><div class="column firstColumn"><h6 class="moduleHeaderLg"><a href="http://www.nytimes.com/pages/national/index.html">U.S. &raquo;</a></h6><ul class="headlinesOnly"><li class="firstItem wrap"><a class="thumb runaroundRight" href="http://www.nytimes.com/2014/02/05/us/politics/budget-office-revises-estimates-of-health-care-enrollment.html?hpw&rref=us"><img src="http://graphics8.nytimes.com/images/2014/02/05/us/jp-HEALTH/jp-HEALTH-thumbStandard.jpg" /></a><h6><a href="http://www.nytimes.com/2014/02/05/us/politics/budget-office-revises-estimates-of-health-care-enrollment.html?hpw&rref=us">Health Care Law Projected to Cut the Labor Force</a></h6></li><li class=""><h6><a  href="http://www.nytimes.com/2014/02/05/us/politics/senate-passes-long-stalled-farm-bill.html?hpw&rref=us">Senate Passes Long-Stalled Farm Bill, With Clear Winners and Losers </a></h6></li><li class="lastItem"><h6><a  href="http://www.nytimes.com/2014/02/05/us/chinese-implicated-in-agricultural-espionage-efforts.html?hpw&rref=us">Designer Seed Thought to Be Latest Target by Chinese</a></h6></li></ul></div><div class="column"><h6 class="moduleHeaderLg"><a href="http://www.nytimes.com/pages/technology/index.html">Technology &raquo;</a></h6><ul class="headlinesOnly"><li class="firstItem wrap"><h6><a  href="http://www.nytimes.com/2014/02/05/technology/new-boss-at-microsoft-with-gates-at-his-side.html?hpw&rref=technology">New Boss at Microsoft, With Gates at His Side</a></h6></li><li class=""><h6><a  href="http://www.nytimes.com/2014/02/05/technology/microsoft-names-engineering-executive-as-new-chief.html?hpw&rref=technology">Microsoft Names New Chief; Gates Becomes Adviser</a></h6></li><li class="lastItem"><h6><a  href="http://bits.blogs.nytimes.com/2014/02/04/the-new-microsoft-is-less-developer-and-more-innovation/?hpw&rref=technology">Bits Blog: With New Chief, Microsoft&rsquo;s New Mantra Is &lsquo;Innovation,&rsquo; Over and Over</a></h6></li></ul></div><div class="column lastColumn"><h6 class="moduleHeaderLg"><a href="http://www.nytimes.com/pages/arts/index.html">Arts &raquo;</a></h6><ul class="headlinesOnly"><li class="firstItem wrap"><a class="thumb runaroundRight" href="http://www.nytimes.com/2014/02/05/arts/design/momas-proposal-for-sculpture-garden-pleases-and-riles.html?hpw&rref=arts"><img src="http://graphics8.nytimes.com/images/2014/02/04/arts/artsspecial/20140205GARDEN-slide-665M/20140205GARDEN-slide-665M-thumbStandard.jpg" /></a><h6><a href="http://www.nytimes.com/2014/02/05/arts/design/momas-proposal-for-sculpture-garden-pleases-and-riles.html?hpw&rref=arts">MoMA&rsquo;s Proposal for Sculpture Garden Pleases and Riles</a></h6></li><li class=""><h6><a  href="http://www.nytimes.com/2014/02/05/books/the-snowden-files-by-luke-harding.html?hpw&rref=arts">Books of The Times: The Needles in the Monumental N.S.A. Haystack</a></h6></li><li class="lastItem"><h6><a  href="http://www.nytimes.com/2014/02/05/arts/president-of-bam-will-leave-next-year.html?hpw&rref=arts">President of BAM Will Leave Next Year</a></h6></li></ul></div></div><div class="module wrap"><div class="column firstColumn"><h6 class="moduleHeaderLg"><a href="http://www.nytimes.com/pages/politics/index.html">Politics  &raquo;</a></h6><ul class="headlinesOnly"><li class="firstItem wrap"><h6><a  href="http://www.nytimes.com/2014/02/05/us/politics/budget-office-revises-estimates-of-health-care-enrollment.html?hpw&rref=politics">Health Care Law Projected to Cut the Labor Force</a></h6></li><li class=""><h6><a  href="http://www.nytimes.com/2014/02/05/us/politics/senate-passes-long-stalled-farm-bill.html?hpw&rref=politics">Senate Passes Long-Stalled Farm Bill, With Clear Winners and Losers </a></h6></li><li class="lastItem"><h6><a  href="http://www.nytimes.com/2014/02/05/us/politics/republicans-spar-on-leaks-and-surveillance-underscoring-partisan-shake-up.html?hpw&rref=politics">Republicans Spar on Leaks and Surveillance, Underscoring Partisan Shake-up</a></h6></li></ul></div><div class="column"><h6 class="moduleHeaderLg"><a href="http://www.nytimes.com/pages/sports/index.html">Sports &raquo;</a></h6><ul class="headlinesOnly"><li class="firstItem wrap"><a class="thumb runaroundRight" href="http://www.nytimes.com/2014/02/05/sports/olympics/so-far-extreme-park-is-proving-extremely-perilous.html?hpw&rref=sports"><img src="http://graphics8.nytimes.com/images/2014/02/05/sports/olympics/05CRASH-slide-KFVO/05CRASH-slide-KFVO-thumbStandard.jpg" /></a><h6><a href="http://www.nytimes.com/2014/02/05/sports/olympics/so-far-extreme-park-is-proving-extremely-perilous.html?hpw&rref=sports">So Far, Extreme Park Is Proving Extremely Perilous</a></h6></li><li class=""><h6><a  href="http://www.nytimes.com/2014/02/05/sports/baseball/with-the-same-old-stadium-same-successful-approach-as-soldier-on.html?hpw&rref=sports">On Baseball: Same Old Stadium, Same Winning Approach for the A&rsquo;s</a></h6></li><li class="lastItem"><h6><a  href="http://www.nytimes.com/2014/02/05/sports/hockey/amid-trade-rumors-callahan-propels-rangers.html?hpw&rref=sports">Rangers 5, Avalanche 1: Amid Trade Rumors, Callahan Propels Rangers</a></h6></li></ul></div><div class="column lastColumn"><h6 class="moduleHeaderLg"><a href="http://www.nytimes.com/pages/movies/index.html">Movies &raquo;</a></h6><ul class="headlinesOnly"><li class="firstItem wrap"><a class="thumb runaroundRight" href="http://www.nytimes.com/2014/02/04/movies/a-o-scott-on-philip-seymour-hoffman.html?hpw&rref=movies"><img src="http://graphics8.nytimes.com/images/2014/02/04/arts/04HOFFMAN/04HOFFMAN-thumbStandard.jpg" /></a><h6><a href="http://www.nytimes.com/2014/02/04/movies/a-o-scott-on-philip-seymour-hoffman.html?hpw&rref=movies">An Appraisal: An Actor Who Made Unhappiness a Joy to Watch</a></h6></li><li class=""><h6><a  href="http://www.nytimes.com/2014/02/04/movies/hollywood-was-just-one-of-his-stages.html?hpw&rref=movies">Hollywood Was Just One of His Stages</a></h6></li><li class="lastItem"><h6><a  href="http://www.nytimes.com/2014/02/05/movies/the-unusual-story-of-tanaquil-le-clercq-artist-and-muse.html?hpw&rref=movies">Movie Review | &#039;Afternoon of a Faun: Tanaquil Le Clercq&#039;: A Dancer&rsquo;s Rare Grace Survives a Horrible Fate</a></h6></li></ul></div></div><div class="module wrap"><div class="column firstColumn"><h6 class="moduleHeaderLg"><a href="http://www.nytimes.com/pages/nyregion/index.html">N.Y. / Region  &raquo;</a></h6><ul class="headlinesOnly"><li class="firstItem wrap"><a class="thumb runaroundRight" href="http://www.nytimes.com/2014/02/05/nyregion/teachers-push-for-back-pay-may-pinch-city.html?hpw&rref=nyregion"><img src="http://graphics8.nytimes.com/images/2014/02/05/nyregion/jpLABOR1/jpLABOR1-thumbStandard-v2.jpg" /></a><h6><a href="http://www.nytimes.com/2014/02/05/nyregion/teachers-push-for-back-pay-may-pinch-city.html?hpw&rref=nyregion">Teachers&rsquo; Push for Back Pay May Pinch New York City</a></h6></li><li class=""><h6><a  href="http://www.nytimes.com/2014/02/05/nyregion/de-blasio-to-skip-st-patricks-day-parade-cites-exclusion-of-gay-groups.html?hpw&rref=nyregion">De Blasio to Skip St. Patrick&rsquo;s Day Parade; Cites Exclusion of Gay Groups</a></h6></li><li class="lastItem"><h6><a  href="http://www.nytimes.com/2014/02/05/nyregion/little-known-regulation-on-tap-water-in-restaurants-is-set-to-fade-away.html?hpw&rref=nyregion">For Restaurants, an Arcane Water Rule Is Going Away </a></h6></li></ul></div><div class="column"><h6 class="moduleHeaderLg"><a href="http://www.nytimes.com/pages/obituaries/index.html">Obituaries &raquo;</a></h6><ul class="headlinesOnly"><li class="firstItem wrap"><a class="thumb runaroundRight" href="http://www.nytimes.com/2014/02/04/us/joan-mondale-former-2nd-lady-dies-at-age-83.html?hpw&rref=obituaries"><img src="http://graphics8.nytimes.com/images/2014/02/04/us/MONDALE-1-obit/MONDALE-1-obit-thumbStandard.jpg" /></a><h6><a href="http://www.nytimes.com/2014/02/04/us/joan-mondale-former-2nd-lady-dies-at-age-83.html?hpw&rref=obituaries">Joan Mondale Dies at 83; Merged Politics With Art</a></h6></li><li class=""><h6><a  href="http://www.nytimes.com/2014/02/04/us/james-j-gallagher-child-development-expert-is-dead-at-87.html?hpw&rref=obituaries">James J. Gallagher, Child Development Expert, Is Dead at 87</a></h6></li><li class="lastItem"><h6><a  href="http://www.nytimes.com/2014/02/04/arts/dance/jean-babilee-dies-at-90-ballets-acrobatic-star.html?hpw&rref=obituaries">Jean Babil&eacute;e, Rebel of World Ballet, Dies at 90</a></h6></li></ul></div><div class="column lastColumn"><h6 class="moduleHeaderLg"><a href="http://theater.nytimes.com/">Theater &raquo;</a></h6><ul class="headlinesOnly"><li class="firstItem wrap"><a class="thumb runaroundRight" href="http://www.nytimes.com/2014/02/05/theater/ghosts-blurred-lines-and-the-pass-in-london.html?hpw&rref=theater"><img src="http://graphics8.nytimes.com/images/2014/02/04/theater/04blurred1/04blurred1-thumbStandard.jpg" /></a><h6><a href="http://www.nytimes.com/2014/02/05/theater/ghosts-blurred-lines-and-the-pass-in-london.html?hpw&rref=theater">Critic&rsquo;s Notebook: In London: Three Plays, Double Standards</a></h6></li><li class=""><h6><a  href="http://www.nytimes.com/2014/02/05/arts/music/michael-john-lachiusa-has-his-night-at-the-allen-room.html?hpw&rref=theater">Music Review: Vignettes From a Much-Lauded Career</a></h6></li><li class="lastItem"><h6><a  href="http://artsbeat.blogs.nytimes.com/2014/02/04/drama-league-fellowship-to-support-female-writer-directors/?hpw&rref=theater">ArtsBeat: Drama League Fellowship to Support Female Writer-Directors</a></h6></li></ul></div></div><div class="module wrap"><div class="column firstColumn"><h6 class="moduleHeaderLg"><a href="http://www.nytimes.com/pages/science/index.html">Science  &raquo;</a></h6><ul class="headlinesOnly"><li class="firstItem wrap"><a class="thumb runaroundRight" href="http://www.nytimes.com/2014/02/04/science/blazing-trails-in-brain-science.html?hpw&rref=science"><img src="http://graphics8.nytimes.com/images/2014/02/04/science/04INSE_SPAN/04INSE-thumbStandard.jpg" /></a><h6><a href="http://www.nytimes.com/2014/02/04/science/blazing-trails-in-brain-science.html?hpw&rref=science">Profiles in Science: Blazing Trails in Brain Science</a></h6></li><li class=""><h6><a  href="http://www.nytimes.com/2014/02/04/science/an-olympian-snow-endeavor-in-sochi.html?hpw&rref=science">An Olympian Snow Endeavor in Sochi</a></h6></li><li class="lastItem"><h6><a  href="http://www.nytimes.com/2014/02/04/science/to-study-aggression-a-fight-club-for-flies.html?hpw&rref=science">To Study Aggression, a Fight Club for Flies</a></h6></li></ul></div><div class="column"><h6 class="moduleHeaderLg"><a href="http://travel.nytimes.com/">Travel &raquo;</a></h6><ul class="headlinesOnly"><li class="firstItem wrap"><a class="thumb runaroundRight" href="http://www.nytimes.com/2014/02/09/travel/familiar-hotel-brands-expand-in-china.html?hpw&rref=travel"><img src="http://graphics8.nytimes.com/images/2014/02/09/travel/09-getaway-span/09-getaway-span-thumbStandard.jpg" /></a><h6><a href="http://www.nytimes.com/2014/02/09/travel/familiar-hotel-brands-expand-in-china.html?hpw&rref=travel">The Getaway: Familiar Hotel Brands Expand in China</a></h6></li><li class=""><h6><a  href="http://www.nytimes.com/2014/02/09/travel/hotel-review-w-singapore.html?hpw&rref=travel">Check In: Hotel Review: W Singapore</a></h6></li><li class="lastItem"><h6><a  href="http://www.nytimes.com/2014/02/04/business/us-airlines-on-time-data-is-incomplete-report-says.html?hpw&rref=travel">Full Picture of Airlines&rsquo; Punctuality Is Elusive</a></h6></li></ul></div><div class="column lastColumn"><h6 class="moduleHeaderLg"><a href="http://www.nytimes.com/pages/arts/television/index.html">Television &raquo;</a></h6><ul class="headlinesOnly"><li class="firstItem wrap"><a class="thumb runaroundRight" href="http://www.nytimes.com/2014/02/05/arts/television/roman-catacomb-mystery-and-super-skyscrapers-on-pbs.html?hpw&rref=television"><img src="http://graphics8.nytimes.com/images/2014/02/05/arts/catacomb1/catacomb1-thumbStandard.jpg" /></a><h6><a href="http://www.nytimes.com/2014/02/05/arts/television/roman-catacomb-mystery-and-super-skyscrapers-on-pbs.html?hpw&rref=television">Critic&rsquo;s Notebook: More Space for the Living and the Dead</a></h6></li><li class=""><h6><a  href="http://www.nytimes.com/2014/02/05/business/media/netflix-signs-for-a-third-season-of-house-of-cards.html?hpw&rref=television">Netflix Signs for a Third Season of &lsquo;House of Cards&rsquo;</a></h6></li><li class="lastItem"><h6><a  href="http://www.nytimes.com/2014/02/02/arts/television/teacher-and-troll-both-start-with-t.html?hpw&rref=television">Television: Teacher and Troll Both Start With &lsquo;T&rsquo;</a></h6></li></ul></div></div><div class="module wrap"><div class="column firstColumn"><h6 class="moduleHeaderLg"><a href="http://www.nytimes.com/pages/health/index.html">Health &raquo;</a></h6><ul class="headlinesOnly"><li class="firstItem wrap"><a class="thumb runaroundRight" href="http://www.nytimes.com/2014/02/05/health/nih-joins-drug-makers-and-nonprofits-on-stubborn-diseases.html?hpw&rref=health"><img src="http://graphics8.nytimes.com/images/2014/02/05/science/05drugs_top/05drugs_top-thumbStandard.jpg" /></a><h6><a href="http://www.nytimes.com/2014/02/05/health/nih-joins-drug-makers-and-nonprofits-on-stubborn-diseases.html?hpw&rref=health">An Unusual Partnership to Tackle Stubborn Diseases</a></h6></li><li class=""><h6><a  href="http://newoldage.blogs.nytimes.com/2014/02/04/what-us-worry/?hpw&rref=health">The New Old Age: What, Us Worry?</a></h6></li><li class="lastItem"><h6><a  href="http://www.nytimes.com/2014/02/04/health/ethics-questions-arise-as-genetic-testing-of-embryos-increases.html?hpw&rref=health">Ethics Questions Arise as Genetic Testing of Embryos Increases</a></h6></li></ul></div><div class="column"><h6 class="moduleHeaderLg"><a href="http://www.nytimes.com/pages/dining/index.html">Dining & Wine &raquo;</a></h6><ul class="headlinesOnly"><li class="firstItem wrap"><a class="thumb runaroundRight" href="http://www.nytimes.com/2014/02/05/dining/restaurant-review-annisa-in-greenwich-village.html?hpw&rref=dining"><img src="http://graphics8.nytimes.com/images/2014/02/05/dining/05REST_395/05REST_395-thumbStandard.jpg" /></a><h6><a href="http://www.nytimes.com/2014/02/05/dining/restaurant-review-annisa-in-greenwich-village.html?hpw&rref=dining">Restaurant Review | Annisa: Keeping Her Passport Handy</a></h6></li><li class=""><h6><a  href="http://www.nytimes.com/2014/02/05/dining/behold-the-sturdy-sheet-pan.html?hpw&rref=dining">A Good Appetite: Behold, the Sturdy Sheet Pan</a></h6></li><li class="lastItem"><h6><a  href="http://www.nytimes.com/2014/02/05/dining/the-seeds-of-a-new-generation.html?hpw&rref=dining">The Seeds of a New Generation</a></h6></li></ul></div><div class="column lastColumn"><h6 class="moduleHeaderLg"><a href="http://www.nytimes.com/pages/books/index.html">Books &raquo;</a></h6><ul class="headlinesOnly"><li class="firstItem wrap"><a class="thumb runaroundRight" href="http://www.nytimes.com/2014/02/05/books/volume-of-robert-frosts-letters-renews-debate-about-his-character.html?hpw&rref=books"><img src="http://graphics8.nytimes.com/images/2014/02/04/arts/design/20140205FROST-slide-LM2N/20140205FROST-slide-LM2N-thumbStandard-v2.jpg" /></a><h6><a href="http://www.nytimes.com/2014/02/05/books/volume-of-robert-frosts-letters-renews-debate-about-his-character.html?hpw&rref=books">The Road Back: Frost&rsquo;s Letters Could Soften a Battered Image</a></h6></li><li class=""><h6><a  href="http://www.nytimes.com/2014/02/09/books/review/how-does-the-classic-marriage-plot-stand-up-in-2014.html?hpw&rref=books">Bookends: How Does the Classic Marriage Plot Stand Up in 2014?</a></h6></li><li class="lastItem"><h6><a  href="http://www.nytimes.com/2014/02/05/books/the-snowden-files-by-luke-harding.html?hpw&rref=books">Books of The Times: The Needles in the Monumental N.S.A. Haystack</a></h6></li></ul></div></div><div class="module wrap"><div class="column firstColumn"><h6 class="moduleHeaderLg"><a href="http://www.nytimes.com/pages/education/index.html">Education &raquo;</a></h6><ul class="headlinesOnly"><li class="firstItem wrap"><h6><a  href="http://www.nytimes.com/2014/02/05/nyregion/teachers-push-for-back-pay-may-pinch-city.html?hpw&rref=education">Teachers&rsquo; Push for Back Pay May Pinch New York City</a></h6></li><li class=""><h6><a  href="http://www.nytimes.com/2014/02/05/education/tennessee-governor-urges-2-free-years-of-community-college-and-technical-school.html?hpw&rref=education">Tennessee Governor Urges 2 Free Years of Community College and Technical School</a></h6></li><li class="lastItem"><h6><a  href="http://www.nytimes.com/2014/02/05/nyregion/assembly-withdraws-bill-to-limit-anti-israel-boycotts.html?hpw&rref=education">Assembly Withdraws Bill to Limit Anti-Israel Boycotts</a></h6></li></ul></div><div class="column"><h6 class="moduleHeaderLg"><a href="http://www.nytimes.com/pages/garden/index.html">Home & Garden &raquo;</a></h6><ul class="headlinesOnly"><li class="firstItem wrap"><a class="thumb runaroundRight" href="http://www.nytimes.com/2014/01/30/garden/a-mystery-at-the-bend.html?hpw&rref=garden"><img src="http://graphics8.nytimes.com/images/2014/01/30/garden/20140130-WHOLIVESTHERE-slide-VR79/20140130-WHOLIVESTHERE-slide-VR79-thumbStandard.jpg" /></a><h6><a href="http://www.nytimes.com/2014/01/30/garden/a-mystery-at-the-bend.html?hpw&rref=garden">Who Lives There: A Mystery at the Bend</a></h6></li><li class=""><h6><a  href="http://www.nytimes.com/2014/01/30/garden/global-design-du-jour.html?hpw&rref=garden">The Details: Global Design Du Jour</a></h6></li><li class="lastItem"><h6><a  href="http://www.nytimes.com/2014/01/30/greathomesanddestinations/the-lure-of-the-hebrides.html?hpw&rref=garden">On Location: Isle of Tiree, Scotland: The Lure of the Hebrides</a></h6></li></ul></div><div class="column lastColumn"><h6 class="moduleHeaderLg"><a href="http://www.nytimes.com/pages/opinion/index.html#sundayreview">Sunday Review &raquo;</a></h6><ul class="headlinesOnly"><li class="firstItem wrap"><a class="thumb runaroundRight" href="http://www.nytimes.com/2014/02/01/opinion/sunday/are-you-my-cousin.html?hpw&rref=opinion"><img src="http://graphics8.nytimes.com/images/2014/02/01/opinion/sunday/01jacobs/01jacobs-thumbStandard-v2.jpg" /></a><h6><a href="http://www.nytimes.com/2014/02/01/opinion/sunday/are-you-my-cousin.html?hpw&rref=opinion">Opinion: Are You My Cousin?</a></h6></li><li class=""><h6><a  href="http://www.nytimes.com/2014/01/26/sunday-review/the-shopping-list-as-policy-tool.html?hpw&rref=opinion">News Analysis: The Shopping List as Policy Tool</a></h6></li><li class="lastItem"><h6><a  href="http://www.nytimes.com/2014/02/02/opinion/sunday/making-surveillance-a-little-less-opaque.html?hpw&rref=opinion">Editorial: Making Surveillance a Little Less Opaque</a></h6></li></ul></div></div><div class="module wrap"><div class="column firstColumn"><h6 class="moduleHeaderLg"><a href="http://www.nytimes.com/pages/realestate/index.html">Real Estate &raquo;</a></h6><ul class="headlinesOnly"><li class="firstItem wrap"><a class="thumb runaroundRight" href="http://www.nytimes.com/2014/02/09/realestate/affordability-in-kensington-brooklyn.html?hpw&rref=realestate"><img src="http://graphics8.nytimes.com/images/2014/02/09/realestate/9-Living/9-Living-thumbStandard.jpg" /></a><h6><a href="http://www.nytimes.com/2014/02/09/realestate/affordability-in-kensington-brooklyn.html?hpw&rref=realestate">Living in: Affordability in Kensington, Brooklyn</a></h6></li><li class=""><h6><a  href="http://www.nytimes.com/2014/02/02/realestate/the-truly-affordable-new-york-apartment.html?hpw&rref=realestate">The Truly Affordable New York Apartment</a></h6></li><li class="lastItem"><h6><a  href="http://www.nytimes.com/2014/02/02/realestate/a-brooklyn-artery-in-transition.html?hpw&rref=realestate">A Brooklyn Artery in Transition</a></h6></li></ul></div><div class="column"><h6 class="moduleHeaderLg"><a href="http://www.nytimes.com/pages/fashion/index.html">Fashion & Style &raquo;</a></h6><ul class="headlinesOnly"><li class="firstItem wrap"><a class="thumb runaroundRight" href="http://www.nytimes.com/video/fashion/100000002686048/colorful-style-in-london.html?hpw&rref=fashion"><img src="http://graphics8.nytimes.com/images/2014/02/03/multimedia/intersection-brixton/intersection-brixton-thumbStandard.jpg" /></a><h6><a href="http://www.nytimes.com/video/fashion/100000002686048/colorful-style-in-london.html?hpw&rref=fashion">Colorful Style in London</a></h6></li><li class=""><h6><a  href="http://www.nytimes.com/2014/02/06/fashion/Swords-Smith-in-Williamsburg-Brooklyn.html?hpw&rref=fashion">Critical Shopper: Hearing Its Own Drummer</a></h6></li><li class="lastItem"><h6><a  href="http://www.nytimes.com/2014/02/02/fashion/SNL-Saturday-Night-Live-Lorne-Michaels-after-party.html?hpw&rref=fashion">Lives of the After-Party</a></h6></li></ul></div><div class="column lastColumn"><h6 class="moduleHeaderLg"><a href="http://www.nytimes.com/pages/magazine/index.html">Magazine &raquo;</a></h6><ul class="headlinesOnly"><li class="firstItem wrap"><a class="thumb runaroundRight" href="http://www.nytimes.com/2014/02/02/magazine/the-post-hope-politics-of-house-of-cards.html?hpw&rref=magazine"><img src="http://graphics8.nytimes.com/images/2014/02/02/magazine/02house1/mag-02House-t_CA0-thumbStandard.jpg" /></a><h6><a href="http://www.nytimes.com/2014/02/02/magazine/the-post-hope-politics-of-house-of-cards.html?hpw&rref=magazine">The Post-Hope Politics of &lsquo;House of Cards&rsquo;</a></h6></li><li class=""><h6><a  href="http://www.nytimes.com/2014/02/09/magazine/can-marriage-cure-poverty.html?hpw&rref=magazine">It&rsquo;s the Economy: Can Marriage Cure Poverty?</a></h6></li><li class="lastItem"><h6><a  href="http://www.nytimes.com/2014/02/02/magazine/confessions-of-a-tiger-couple.html?hpw&rref=magazine">Confessions of a Tiger Couple</a></h6></li></ul></div></div><div class="module wrap"><div class="column"><h6 class="moduleHeaderLg"><a href="http://www.nytimes.com/pages/automobiles/index.html">Automobiles &raquo;</a></h6><ul class="headlinesOnly"><li class="firstItem wrap"><a class="thumb runaroundRight" href="http://www.nytimes.com/2014/02/02/automobiles/collectibles/a-hand-me-down-with-a-history.html?hpw&rref=automobiles"><img src="http://graphics8.nytimes.com/images/2014/02/02/automobiles/EGO1/EGO1-thumbStandard-v2.jpg" /></a><h6><a href="http://www.nytimes.com/2014/02/02/automobiles/collectibles/a-hand-me-down-with-a-history.html?hpw&rref=automobiles">Auto Ego: A Hand-Me-Down With a History</a></h6></li><li class=""><h6><a  href="http://www.nytimes.com/2014/02/02/automobiles/autoreviews/german-lessons-are-paying-off.html?hpw&rref=automobiles">Behind the Wheel | 2014 Cadillac CTS: The German Lessons Are Paying Off</a></h6></li><li class="lastItem"><h6><a  href="http://www.nytimes.com/2014/02/02/automobiles/autoreviews/vsport-the-bmw-beater.html?hpw&rref=automobiles">CTS Vsport: The BMW Beater</a></h6></li></ul></div><div class="column lastColumn"><h6 class="moduleHeaderLg"><a href="http://www.nytimes.com/pages/t-magazine/index.html">T Magazine  &raquo;</a></h6><ul class="headlinesOnly"><li class="firstItem wrap"><a class="thumb runaroundRight" href="http://tmagazine.blogs.nytimes.com/2014/02/04/threes-a-trend-luxe-sweatpants/?hpw&rref=t-magazine"><img src="http://graphics8.nytimes.com/images/2014/02/04/t-magazine/04sweat-pask/04sweat-pask-thumbStandard-v2.jpg" /></a><h6><a href="http://tmagazine.blogs.nytimes.com/2014/02/04/threes-a-trend-luxe-sweatpants/?hpw&rref=t-magazine">Three&rsquo;s a Trend | Luxe Sweatpants</a></h6></li><li class=""><h6><a  href="http://tmagazine.blogs.nytimes.com/2014/02/04/listen-up-singer-songwriter-jenny-lewiss-perfect-new-single-for-girls/?hpw&rref=t-magazine">Listen Up | Singer-Songwriter Jenny Lewis&rsquo;s Perfect New Single for &lsquo;Girls&rsquo;</a></h6></li><li class="lastItem"><h6><a  href="http://tmagazine.blogs.nytimes.com/2014/02/04/food-matters-hot-dog/?hpw&rref=t-magazine">Food Matters | Hot Dog!</a></h6></li></ul></div></div></div>
&nbsp;
</div><!--close abColumn -->
<div class="cColumn">

<div class="columnGroup first">

    <a name="timeswire"></a>
    <div class="timeswireModule">
        <h4 class="sectionHeaderHome"><a href="http://www.nytimes.com/timeswire/?src=twrhp">Times Wire &raquo;</a></h4>
        <p class="refer">Most recent updates on NYTimes.com. <a href="http://www.nytimes.com/timeswire/?src=twr" title="Go to Times Wire">See More &raquo;</a></p>
        <ol id="wireContent" class="singleRule">
            <li class='wrap'><span class='timestamp' title='2014-02-04 23:25:11' data-gmt='1391574311'>11:25 PM ET</span> <a href='http://www.nytimes.com/2014/02/05/opinion/edsall-free-trade-disagreement.html?src=twrhp'>Free Trade Disagreement</a></li>
            <li class='wrap'><span class='timestamp' title='2014-02-04 23:23:05' data-gmt='1391574185'>11:23 PM ET</span> <a href='http://www.nytimes.com/2014/02/05/world/asia/old-tensions-resurface-in-debate-over-us-role-in-post-2014-afghanistan.html?src=twrhp'>Old Tensions Resurface in Debate Over U.S. Role in Post-2014 Afghanistan</a></li>
            <li class='wrap last'><span class='timestamp' title='2014-02-04 23:20:22' data-gmt='1391574022'>11:20 PM ET</span> <a href='http://www.nytimes.com/2014/02/05/us/california-proposal-for-lucas-museum-is-rejected.html?src=twrhp'>California: Proposal for Lucas Museum Is Rejected</a></li>
        </ol>
    </div>
    <div class="singleRuleDivider"></div>
    </div>
<div class="columnGroup ">
<div id="mostPopWidget" class="doubleRule"></div>
<script src="http://js.nyt.com/js/app/recommendations/recommendationsModule.js" type="text/javascript" charset="utf-8"></script>
</div>
<div class="columnGroup ">

<div class="singleAd" id="Box1">
<!-- ADXINFO classification="Big_Ad_-_Standard" campaign="nyt2014_300x250_mod_store" priority="1000" isInlineSafe="N" width="300" height="250" --><a href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=Box1&sn2=5b35dc29/56a295e7&sn1=e97936d7/abca7d27&camp=nyt2014_300x250_mod_store&ad=2/3_300x250_storeVDay&goto=http%3A%2F%2Fwww%2Enytstore%2Ecom%2Fvalentine%3Futm%5Fsource%3Dnytimes%26utm%5Fmedium%3Dhouse%2Dad%26utm%5Fterm%3Dvalentines%2D300x79%26utm%5Fcontent%3Dros%26utm%5Fcampaign%3D1%2D23%2D14" target="_blank">
<img src="http://graphics8.nytimes.com/adx/images/ADS/36/30/ad.363070/14-2642-NYTS_VDay_300x250_MS3.jpg" width="300" height="250" border="0">
</a>
</div>

</div>
<div class="columnGroup ">

<div class="singleAd" id="HPBottom1">
<!-- ADXINFO classification="Text_Link" campaign="nyt2013_storemodule_nytstore_hp" priority="1002" isInlineSafe="Y" width="0" height="0" --><div class="singleAd" id="HPBottom1">


<style type="text/css">
        #HPBottom1 div a,
        #HPBottom1 .storeLink {
          text-decoration: none;
        }  
        
        #HPBottom1 div a:hover {
          text-decoration: underline;
        }

        #HPBottom1 .itemHeader,
        #HPBottom1 .itemDescription,
        #HPBottom1 .itemPrice,
        #HPBottom1 .storeOffer,
        #HPBottom1 .storeLink {
          font-family: "nyt-franklin",arial,helvetica,sans-serif;  
        }

        #HPBottom1 .itemHeader,
        #HPBottom1 .itemPrice,
        #HPBottom1 .storeOffer,
        #HPBottom1 .storeLink  {
          font-weight: 700;  
        }

        #HPBottom1 .itemDescription {
          font-weight: 500; 
        }  

        #HPBottom1 .itemHeader,
        #HPBottom1 .itemDescription,
        #HPBottom1 .itemPrice,
        #HPBottom1 .storeOffer,
        #HPBottom1 .storeLink {
          font-size: 12px;
        }

        #HPBottom1 .itemHeader {
          font-size: 14px; 
        }  

        #HPBottom1 .itemDescription {
          color: #777; 
          margin-top: 3px;
        }

        #HPBottom1 .itemPrice {
          color: #0c4472;
        }

        #HPBottom1 .itemHeader,
        #HPBottom1 .storeLink {
          color: #000; 
        }
        </style>
      <table cellpadding="5" cellspacing="5" width="375px" height="auto" style="border: 1px solid #c9c9c9; padding: 5px;">
          <tbody>
            <tr>
              <td align="center" colspan="2" style="padding: 0;">
                <a href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=HPBottom1&sn2=ba5a7590/f9c69a68&sn1=4cfe2ecf/9dc0cc3d&camp=nyt2013_storemodule_nytstore_hp&ad=nyt5_loving_puzzle&goto=http%3A%2F%2Fwww%2Enytstore%2Ecom%2F%3Futm%5Fsource%3Dnytimes%26utm%5Fmedium%3DHPB%26utm%5Fcontent%3DHero%5Fstore%5Ftop%5Floving%2Dpuzzle%26utm%5Fcampaign%3DNYT%2DWinter" target="_blank"><img src="http://graphics8.nytimes.com/adx/images/ADS/36/30/ad.363027/nytstore-header.PNG" alt="The New York Times Store"></a>
              </td>
            </tr>
            <tr>
              <td width="40%" style="padding-right: 0;  padding-top: 7px; padding-left: 5px;">
               <a href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=HPBottom1&sn2=ba5a7590/f9c69a68&sn1=4cfe2ecf/9dc0cc3d&camp=nyt2013_storemodule_nytstore_hp&ad=nyt5_loving_puzzle&goto=http%3A%2F%2Fwww%2Enytstore%2Ecom%2FLoving%2DThoughts%2DWooden%2DJigsaw%2DPuzzle%5Fp%5F11321%2Ehtml%3Futm%5Fsource%3Dnytimes%26utm%5Fmedium%3DHPB%26utm%5Fcontent%3DHero%5Fimage%5Floving%2Dpuzzle%26utm%5Fcampaign%3DNYT%2DWinter" target="_blank"><img src="http://graphics8.nytimes.com/adx/images/ADS/36/30/ad.363027/1-30-14_loving-puzzle.jpg" style="height: 150px; width: 150px;" alt="The New York Times Store"></a>
              </td>
              <td width="60%" style="padding-right: 0; position: relative; vertical-align: text-top;">
                <div style="margin-top: 10px; margin-bottom:5px;">
                  <a class="itemHeader" href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=HPBottom1&sn2=ba5a7590/f9c69a68&sn1=4cfe2ecf/9dc0cc3d&camp=nyt2013_storemodule_nytstore_hp&ad=nyt5_loving_puzzle&goto=http%3A%2F%2Fwww%2Enytstore%2Ecom%2Fvalentine%3Futm%5Fsource%3Dnytimes%26utm%5Fmedium%3DHPB%26utm%5Fcontent%3DHero%5Fdepartment%5Floving%2Dpuzzle%26utm%5Fcampaign%3DNYT%2DWinter" target="_blank">Valentine's Day Gifts</a>
                </div>
                <div style="margin-top: 5px; margin-bottom:5px;">
                  <a class="itemDescription" style="font-weight: 700;" href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=HPBottom1&sn2=ba5a7590/f9c69a68&sn1=4cfe2ecf/9dc0cc3d&camp=nyt2013_storemodule_nytstore_hp&ad=nyt5_loving_puzzle&goto=http%3A%2F%2Fwww%2Enytstore%2Ecom%2FLoving%2DThoughts%2DWooden%2DJigsaw%2DPuzzle%5Fp%5F11321%2Ehtml%3Futm%5Fsource%3Dnytimes%26utm%5Fmedium%3DHPB%26utm%5Fcontent%3DHero%5Fproduct%5Floving%2Dpuzzle%26utm%5Fcampaign%3DNYT%2DWinter" target="_blank">Loving Thoughts Wooden Jigsaw Puzzle</a>
</div>
<div><a class="itemDescription" href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=HPBottom1&sn2=ba5a7590/f9c69a68&sn1=4cfe2ecf/9dc0cc3d&camp=nyt2013_storemodule_nytstore_hp&ad=nyt5_loving_puzzle&goto=http%3A%2F%2Fwww%2Enytstore%2Ecom%2FLoving%2DThoughts%2DWooden%2DJigsaw%2DPuzzle%5Fp%5F11321%2Ehtml%3Futm%5Fsource%3Dnytimes%26utm%5Fmedium%3DHPB%26utm%5Fcontent%3DHero%5Fproduct%5Floving%2Dpuzzle%26utm%5Fcampaign%3DNYT%2DWinter" target="_blank">Give your sweetheart a gift to last a lifetime! This puzzle is made in America and no two pieces are the same.</a></div>
                <div style="margin-top: 5px;">
                  <a class="itemPrice" href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=HPBottom1&sn2=ba5a7590/f9c69a68&sn1=4cfe2ecf/9dc0cc3d&camp=nyt2013_storemodule_nytstore_hp&ad=nyt5_loving_puzzle&goto=http%3A%2F%2Fwww%2Enytstore%2Ecom%2FLoving%2DThoughts%2DWooden%2DJigsaw%2DPuzzle%5Fp%5F11321%2Ehtml%3Futm%5Fsource%3Dnytimes%26utm%5Fmedium%3DHPB%26utm%5Fcontent%3DHero%5Fproduct%5Floving%2Dpuzzle%26utm%5Fcampaign%3DNYT%2DWinter" target="_blank">$79.00</a>
                </div>
                <div style="margin-top: 18px;">
                  <a class="storeLink" href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=HPBottom1&sn2=ba5a7590/f9c69a68&sn1=4cfe2ecf/9dc0cc3d&camp=nyt2013_storemodule_nytstore_hp&ad=nyt5_loving_puzzle&goto=http%3A%2F%2Fwww%2Enytstore%2Ecom%2F%3Futm%5Fsource%3Dnytimes%26utm%5Fmedium%3DHPB%26utm%5Fcontent%3DHero%5Fstore%5Fbottom%5Floving%2Dpuzzle%26utm%5Fcampaign%3DNYT%2DWinter" target="_blank">NYTStore.com &#187;</a>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
</div>
</div>

</div>
<div class="columnGroup ">

<div class="singleAd" id="HPBottom2">
<!-- ADXINFO classification="Text_Link" campaign="nyt2013_footer_hd_hp_ros_34QQH" priority="1000" isInlineSafe="Y" width="0" height="0" --><style>
#hpb2-wrapper {
  width: 100%;
  float: left;
  clear: both;
  padding-bottom: 10px;
}
#hpb2-thumb {
  width: 45px;
  height: 28px;
  float: left;
  margin-right: 5px;
}
#hpb2-callout {
  width: 325px;
  float: left;
  clear: none;
  font-family: "nyt-franklin","helvetica neue",arial,sans-serif;
  margin-top: 7px;
  font-size: 0.75rem;
}
</style>

<div id="hpb2-wrapper">
  <div id="hpb2-thumb">
    <a href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=HPBottom2&sn2=ba5a7591/f9ca9a68&sn1=69e02372/71b54476&camp=nyt2013_footer_hd_hp_ros_34QQH&ad=hp_footer_hd_20141123_get50off_34QQH&goto=https%3A%2F%2Fwww%2Enytimesathome%2Ecom%2Fhd%2F101%3FSPTR%5FID%3DhdNYT%26MediaCode%3DW42CQ%26CMP%3D34QQH" target="_blank"><img src="http://graphics8.nytimes.com/adx/images/ADS/36/22/ad.362278/icon-newspaper.jpg" alt="Get 50% Off The New York Times &amp; Free All Digital Access"></a>
  </div>

  <p id="hpb2-callout"><a href="http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=homepage.nytimes.com/index.html&pos=HPBottom2&sn2=ba5a7591/f9ca9a68&sn1=69e02372/71b54476&camp=nyt2013_footer_hd_hp_ros_34QQH&ad=hp_footer_hd_20141123_get50off_34QQH&goto=https%3A%2F%2Fwww%2Enytimesathome%2Ecom%2Fhd%2F101%3FSPTR%5FID%3DhdNYT%26MediaCode%3DW42CQ%26CMP%3D34QQH" target="_blank">Get 50% Off The New York Times &amp; Free All Digital Access.</a></p>
</div>
</div>

</div>
<div class="columnGroup ">

</div>
<div class="columnGroup last">

<div class="singleAd" id="SponLinkHP">
<!-- ADXINFO classification="Featured_Product_Image" campaign="Google_AdSense_HP_14" priority="1002" isInlineSafe="N" width="120" height="90" --><script language="JavaScript" type="text/javascript">
// rev6_GoogleHP.html.new
<!--
function cs(){window.status='';}function ha(a){  pha=document.getElementById(a); nhi=pha.href.indexOf("&nh=");if(nhi < 1) {phb=pha.href+"&nh=1";} pha.href=phb;}function ca(a) {  pha=document.getElementById(a); nci=pha.href.indexOf("&nc=");if(nci < 1) {phb=pha.href+"&nc=1";} pha.href=phb;window.open(document.getElementById(a).href);}function ga(o,e) {if (document.getElementById) {a=o.id.substring(1);p = "";r = "";g = e.target;if (g) {t = g.id;f = g.parentNode;if (f) {p = f.id;h = f.parentNode;if (h)r = h.id;}} else {h = e.srcElement;f = h.parentNode;if (f)p = f.id;t = h.id;}if (t==a || p==a || r==a)return true;pha=document.getElementById(a); nbi=pha.href.indexOf("&nb=");if(nbi < 1) {phb=pha.href+"&nb=1";} pha.href=phb;window.open(document.getElementById(a).href);}}

function randHPWell() {
	var wells = new Array("hpwell_travel","hpwell_automobiles");
	var ar_id = wells[Math.floor(Math.random()*wells.length)]+parseInt(1+Math.floor(Math.random()*3));
	if (document.getElementById(ar_id)) { return document.getElementById(ar_id).href; } else { return "http://www.nytimes.com";}
}

function google_ad_request_done(ads) {
	var s = "";

	if (ads.length == 0) {
		return;
	} else if (ads.length == 1 && ads[0].type != 'image') {
		google_ad_section_line_height = "22px";
		google_ad_section_padding_left = "12px";
		google_title_link_font_size = "18px";
		google_ad_text_font_size = "14px";
		google_visible_url_font_size = "14px";
		google_target_div = 'SponLinkHP';
	} else if (ads[0].type != 'image') {
		google_ad_section_line_height = "14px";
		google_ad_section_padding_left = "7px";
		google_title_link_font_size = "12px";
		google_ad_text_font_size = "11px";
		google_visible_url_font_size = "10px";
		google_target_div = 'SponLinkHP';
	}
	s += '<table width="100%" height="" border="0" cellspacing="0" cellpadding="0" style="width:100%; border-style: solid; border-width: 1px; border-color: #9da3ad" >\n<tr>\n<td style="font-family:Arial,Helvetica,sans-serif; font-size:12px; color:#333333;" valign="top"><table width="100%" height="100%" cellspacing="0" cellpadding="0" border="0" style="width:100%; height:100%;">\n<tr>\n <td style="background-color:#9da3ad; width:70%; height:20px; padding-top:2px; padding-left:11px; padding-bottom:2px; font-family:Arial,Helvetica,sans-serif; font-size:12px; color:#333333;" width="70%" height="20" bgcolor="#9da3ad" ><span style="font-size: 12px; font-weight: normal; color:#ffffff;" >Ads by Google</span></td>\n<td style="padding-top:2px; padding-bottom:2px; width:30%; height:20px; align:right; background-color:#9da3ad; font-family:Arial,Helvetica,sans-serif; font-size:12px; color:#333333;" width="30%" height="20" align="right" bgcolor="#9da3ad" ><span><a style="font-family:Arial,Helvetica,sans-serif; color: white; font-size:12px; padding-right:7px;" href="http://www.nytimes.com/ref/membercenter/faq/linkingqa16.html" onclick="window.open(\'\',\'popupad\',\'left=100,top=100,width=390,height=390,resizable,scrollbars=no\')" target="popupad">what\'s this?</a></span></td>\n</tr>\n</table>\n</td>\n</tr>\n<tr>\n<td style="height:110px; font-family:Arial,Helvetica,sans-serif; font-size:12px; color:#333333;" valign="top" height="110"><table height="100%" width="100%" cellpadding="4" cellspacing="0" border="0" bgcolor="#f8f8f9" style="height:100%; width:100%; padding:4px; background-color:#f8f8f9;">\n';
	for (i = 0; i < ads.length; ++i) {
	   s += '<tr>\n<td style="font-family:Arial,Helvetica,sans-serif; font-size:12px; color:#333333; background-color:#f8f8f9;" valign="middle" >\n<div style="line-height:' + google_ad_section_line_height + '; padding-left:' + google_ad_section_padding_left + '; padding-bottom:5px;" >\n<a href="' + ads[i].url + '" target="_blank" style="font-size:' + google_title_link_font_size + '; color:#000066; font-weight:bold; text-decoration:underline;"> ' + ads[i].line1 + '</a><br>\n' + ads[i].line2 + ' ' + ads[i].line3 + '<br>\n<a href="' + ads[i].url + '" target="_blank" style="font-size:' + google_visible_url_font_size + '; color:#000066; font-weight:normal; text-decoration:none;">' + ads[i].visible_url + '</a>\n</div>\n </td>\n</tr>\n';
	}
	s += '</table>\n</td>\n</tr>\n</table>';
	document.getElementById(google_target_div).innerHTML = s;
	return;
}
google_ad_output = 'js';
google_max_num_ads = '3';
google_ad_client = 'ca-nytimes_homepage_js';
google_safe = 'high';
google_ad_channel = 'pg_url_test';
google_targeting = 'content';
if (window.nyt_google_count) { google_skip = nyt_google_count; }
google_ad_section = 'default';
google_hints = 'business news online,us news online,online us news,top online news,business international news,online latest news';
// -->
</script>

<script type="text/javascript" language="JavaScript" src="http://pagead2.googlesyndication.com/pagead/show_ads.js"></script>
</div>

</div>
</div><!--close cColumn -->
</div><!--close spanAB -->
</div><!--close column -->
</div><!--close doubleRule -->
</div><!--close baseLayout -->
</div><!--close main -->
<footer class="pageFooter">
<div class="inset">
<nav class="pageFooterNav">
<ul class="pageFooterNavList wrap">
<li class="firstItem"><a href="http://www.nytco.com/">&copy; 2014 The New York Times Company</a></li>
<li><a href="http://spiderbites.nytimes.com/">Site Map</a></li>
<li><a href="http://www.nytimes.com/privacy">Privacy</a></li>
<li><a href="http://www.nytimes.com/ref/membercenter/help/privacy.html#pp">Your Ad Choices</a></li>
<li><a href="http://www.nytimes.whsites.net/mediakit/">Advertise</a></li>
<li><a href="http://www.nytimes.com/content/help/rights/sale/terms-of-sale.html ">Terms of Sale</a></li>
<li><a href="http://www.nytimes.com/ref/membercenter/help/agree.html">Terms of Service</a></li>
<li><a href="http://www.nytco.com/careers">Work With Us</a></li>
<li><a href="http://www.nytimes.com/rss">RSS</a></li>
<li><a href="http://www.nytimes.com/membercenter/sitehelp.html">Help</a></li>
<li><a href="http://www.nytimes.com/ref/membercenter/help/infoservdirectory.html">Contact Us</a></li>
<li class="lastItem"><a href="/membercenter/feedback.html">Site Feedback</a></li>
</ul>
</nav>
</div><!--close inset -->
</footer><!--close pageFooter -->
</div><!--close page -->
</div><!--close shell -->
<script type = "text/javascript" language = "JavaScript">
    var NYTArticleCommentCounts = {"http:\/\/www.nytimes.com\/2014\/02\/05\/nyregion\/teachers-push-for-back-pay-may-pinch-city.html":{"count":1,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/05\/nyregion\/teachers-push-for-back-pay-may-pinch-city.html"},"http:\/\/www.nytimes.com\/2014\/02\/05\/books\/volume-of-robert-frosts-letters-renews-debate-about-his-character.html":{"count":0,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/05\/books\/volume-of-robert-frosts-letters-renews-debate-about-his-character.html"},"http:\/\/www.nytimes.com\/2014\/02\/09\/books\/review\/how-does-the-classic-marriage-plot-stand-up-in-2014.html":{"count":0,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/09\/books\/review\/how-does-the-classic-marriage-plot-stand-up-in-2014.html"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/02\/04\/from-shadows-to-citizenship\/immigrants-without-a-path-to-citizenship-a-permanent-underclass":{"count":0,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/02\/04\/from-shadows-to-citizenship\/immigrants-without-a-path-to-citizenship-a-permanent-underclass"},"http:\/\/www.nytimes.com\/2014\/02\/05\/opinion\/bittman-just-say-no.html":{"count":1,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/05\/opinion\/bittman-just-say-no.html"},"http:\/\/www.nytimes.com\/2014\/02\/05\/opinion\/freeing-workers-from-the-insurance-trap.html":{"count":3,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/05\/opinion\/freeing-workers-from-the-insurance-trap.html"},"http:\/\/www.nytimes.com\/2014\/02\/05\/opinion\/dowd-high-school-maniacal.html":{"count":5,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/05\/opinion\/dowd-high-school-maniacal.html"},"http:\/\/www.nytimes.com\/2014\/02\/05\/opinion\/friedman-the-third-intifada.html":{"count":2,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/05\/opinion\/friedman-the-third-intifada.html"},"http:\/\/www.nytimes.com\/2014\/02\/05\/world\/asia\/philippine-leader-urges-international-help-in-resisting-chinas-sea-claims.html":{"count":78,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/05\/world\/asia\/philippine-leader-urges-international-help-in-resisting-chinas-sea-claims.html"},"http:\/\/www.nytimes.com\/2014\/02\/05\/dining\/restaurant-review-annisa-in-greenwich-village.html":{"count":3,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/05\/dining\/restaurant-review-annisa-in-greenwich-village.html"},"http:\/\/travel.nytimes.com\/2014\/02\/09\/travel\/familiar-hotel-brands-expand-in-china.html":{"count":0,"commentsEnabled":true,"assetUrl":"http:\/\/travel.nytimes.com\/2014\/02\/09\/travel\/familiar-hotel-brands-expand-in-china.html"},"http:\/\/www.nytimes.com\/2014\/02\/05\/books\/the-snowden-files-by-luke-harding.html":{"count":16,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/05\/books\/the-snowden-files-by-luke-harding.html"},"http:\/\/www.nytimes.com\/2014\/02\/05\/technology\/microsoft-names-engineering-executive-as-new-chief.html":{"count":11,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/05\/technology\/microsoft-names-engineering-executive-as-new-chief.html"},"http:\/\/www.nytimes.com\/2014\/02\/05\/us\/politics\/senate-passes-long-stalled-farm-bill.html":{"count":146,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/05\/us\/politics\/senate-passes-long-stalled-farm-bill.html"},"http:\/\/www.nytimes.com\/2014\/02\/05\/dining\/at-bouley-botanical-planters-overflow.html":{"count":1,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/05\/dining\/at-bouley-botanical-planters-overflow.html"},"http:\/\/www.nytimes.com\/2014\/02\/05\/dining\/behold-the-sturdy-sheet-pan.html":{"count":13,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/05\/dining\/behold-the-sturdy-sheet-pan.html"},"http:\/\/www.nytimes.com\/2014\/02\/05\/dining\/the-seeds-of-a-new-generation.html":{"count":28,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/05\/dining\/the-seeds-of-a-new-generation.html"},"http:\/\/www.nytimes.com\/2014\/02\/05\/sports\/baseball\/with-the-same-old-stadium-same-successful-approach-as-soldier-on.html":{"count":2,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/05\/sports\/baseball\/with-the-same-old-stadium-same-successful-approach-as-soldier-on.html"},"http:\/\/www.nytimes.com\/news\/minute\/2014\/02\/04\/times-minute-microsofts-new-c-e-o\/":{"count":0,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/news\/minute\/2014\/02\/04\/times-minute-microsofts-new-c-e-o\/"},"http:\/\/www.nytimes.com\/2014\/02\/04\/your-money\/paying-the-rent-on-time-can-enhance-your-credit-report.html":{"count":1,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/04\/your-money\/paying-the-rent-on-time-can-enhance-your-credit-report.html"},"http:\/\/www.nytimes.com\/2014\/02\/09\/magazine\/can-marriage-cure-poverty.html":{"count":53,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/09\/magazine\/can-marriage-cure-poverty.html"},"http:\/\/www.nytimes.com\/2014\/02\/05\/us\/politics\/budget-office-revises-estimates-of-health-care-enrollment.html":{"count":1188,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/05\/us\/politics\/budget-office-revises-estimates-of-health-care-enrollment.html"},"http:\/\/www.nytimes.com\/2014\/02\/09\/education\/edlife\/a-historically-black-college-is-rocked-by-the-economy-infighting-and-a-changing-demographic.html":{"count":103,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/09\/education\/edlife\/a-historically-black-college-is-rocked-by-the-economy-infighting-and-a-changing-demographic.html"},"http:\/\/www.nytimes.com\/2014\/02\/05\/sports\/olympics\/minnesotas-olympic-hockey-cradle-pop-1781.html":{"count":22,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/05\/sports\/olympics\/minnesotas-olympic-hockey-cradle-pop-1781.html"},"http:\/\/www.nytimes.com\/2014\/02\/04\/booming\/the-booming-blog-says-goodbye.html":{"count":88,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/04\/booming\/the-booming-blog-says-goodbye.html"},"http:\/\/www.nytimes.com\/2014\/02\/04\/booming\/remembering-to-pray.html":{"count":25,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/04\/booming\/remembering-to-pray.html"},"http:\/\/www.nytimes.com\/2014\/02\/04\/opinion\/krauze-mexicos-vigilantes-on-the-march.html":{"count":14,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/04\/opinion\/krauze-mexicos-vigilantes-on-the-march.html"},"http:\/\/www.nytimes.com\/2014\/02\/04\/opinion\/dont-let-putin-grab-ukraine.html":{"count":17,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/04\/opinion\/dont-let-putin-grab-ukraine.html"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/02\/03\/the-casual-couture-of-the-average-american\/free-your-style-free-your-thoughts":{"count":13,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/02\/03\/the-casual-couture-of-the-average-american\/free-your-style-free-your-thoughts"},"http:\/\/www.nytimes.com\/2014\/02\/04\/booming\/stevie-nicks-just-following-her-muse.html":{"count":36,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/04\/booming\/stevie-nicks-just-following-her-muse.html"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/02\/03\/the-casual-couture-of-the-average-american\/casual-dress-has-gone-global":{"count":26,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/02\/03\/the-casual-couture-of-the-average-american\/casual-dress-has-gone-global"},"http:\/\/www.nytimes.com\/2014\/02\/05\/dining\/take-a-dumpling-detour.html":{"count":3,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/05\/dining\/take-a-dumpling-detour.html"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/02\/03\/the-casual-couture-of-the-average-american\/t-shirts-and-jeans-pure-american-style":{"count":25,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/02\/03\/the-casual-couture-of-the-average-american\/t-shirts-and-jeans-pure-american-style"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/02\/03\/the-casual-couture-of-the-average-american\/clothes-complete-the-brand":{"count":29,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/02\/03\/the-casual-couture-of-the-average-american\/clothes-complete-the-brand"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/02\/03\/the-casual-couture-of-the-average-american\/sartorial-decisions-have-repercussions":{"count":55,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/02\/03\/the-casual-couture-of-the-average-american\/sartorial-decisions-have-repercussions"},"http:\/\/www.nytimes.com\/2014\/02\/04\/world\/asia\/karzai-has-held-secret-contacts-with-the-taliban.html":{"count":325,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/04\/world\/asia\/karzai-has-held-secret-contacts-with-the-taliban.html"},"http:\/\/www.nytimes.com\/2014\/02\/04\/nyregion\/hoffmans-heroin-points-to-surge-in-grim-trade.html":{"count":540,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/04\/nyregion\/hoffmans-heroin-points-to-surge-in-grim-trade.html"},"http:\/\/www.nytimes.com\/2014\/02\/04\/opinion\/when-loud-music-turned-deadly.html":{"count":132,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/04\/opinion\/when-loud-music-turned-deadly.html"},"http:\/\/www.nytimes.com\/2014\/02\/04\/health\/ethics-questions-arise-as-genetic-testing-of-embryos-increases.html":{"count":481,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/04\/health\/ethics-questions-arise-as-genetic-testing-of-embryos-increases.html"},"http:\/\/www.nytimes.com\/2014\/02\/04\/us\/politics\/obama-moves-to-the-right-in-a-partisan-war-of-words.html":{"count":185,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/04\/us\/politics\/obama-moves-to-the-right-in-a-partisan-war-of-words.html"},"http:\/\/www.nytimes.com\/2014\/02\/04\/opinion\/the-mayor-and-the-unions.html":{"count":232,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/04\/opinion\/the-mayor-and-the-unions.html"},"http:\/\/www.nytimes.com\/2014\/02\/04\/opinion\/dont-ask-your-doctor-about-low-t.html":{"count":335,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/04\/opinion\/dont-ask-your-doctor-about-low-t.html"},"http:\/\/www.nytimes.com\/2014\/02\/04\/opinion\/nocera-the-gun-report-1-year-later.html":{"count":414,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/04\/opinion\/nocera-the-gun-report-1-year-later.html"},"http:\/\/www.nytimes.com\/2014\/02\/04\/opinion\/cohen-the-talks-round-two.html":{"count":124,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/04\/opinion\/cohen-the-talks-round-two.html"},"http:\/\/www.nytimes.com\/2014\/02\/04\/opinion\/brooks-what-machines-cant-do.html":{"count":299,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/04\/opinion\/brooks-what-machines-cant-do.html"},"http:\/\/www.nytimes.com\/2014\/02\/04\/nyregion\/citys-parks-department-takes-a-seat-behind-nonprofit-conservancies.html":{"count":62,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/04\/nyregion\/citys-parks-department-takes-a-seat-behind-nonprofit-conservancies.html"},"http:\/\/www.nytimes.com\/2014\/02\/04\/opinion\/bruni-love-death-and-sochi.html":{"count":142,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/04\/opinion\/bruni-love-death-and-sochi.html"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/02\/03\/the-casual-couture-of-the-average-american\/the-60s-changed-everything-in-american-style":{"count":106,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/02\/03\/the-casual-couture-of-the-average-american\/the-60s-changed-everything-in-american-style"},"http:\/\/www.nytimes.com\/2014\/02\/04\/nyregion\/flocking-to-trains-super-bowl-fans-overwhelmed-transit-system.html":{"count":88,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/04\/nyregion\/flocking-to-trains-super-bowl-fans-overwhelmed-transit-system.html"},"http:\/\/www.nytimes.com\/2014\/02\/04\/business\/us-airlines-on-time-data-is-incomplete-report-says.html":{"count":28,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/04\/business\/us-airlines-on-time-data-is-incomplete-report-says.html"},"http:\/\/www.nytimes.com\/2014\/02\/05\/dining\/in-india-a-pilgrimage-to-a-feast-for-thousands.html":{"count":19,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/05\/dining\/in-india-a-pilgrimage-to-a-feast-for-thousands.html"},"http:\/\/www.nytimes.com\/2014\/02\/04\/us\/push-for-preschool-becomes-a-bipartisan-cause-outside-washington.html":{"count":124,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/04\/us\/push-for-preschool-becomes-a-bipartisan-cause-outside-washington.html"},"http:\/\/www.nytimes.com\/news\/minute\/2014\/02\/03\/times-minute-making-snow-for-sochi\/":{"count":0,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/news\/minute\/2014\/02\/03\/times-minute-making-snow-for-sochi\/"},"http:\/\/www.nytimes.com\/2014\/02\/04\/world\/asia\/after-typhoons-devastation-a-philippine-town-is-losing-those-who-could-rebuild-it.html":{"count":22,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/04\/world\/asia\/after-typhoons-devastation-a-philippine-town-is-losing-those-who-could-rebuild-it.html"},"http:\/\/www.nytimes.com\/2014\/02\/05\/dining\/cutting-straight-to-the-chase-with-dessert.html":{"count":14,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/05\/dining\/cutting-straight-to-the-chase-with-dessert.html"},"http:\/\/www.nytimes.com\/2014\/02\/04\/sports\/olympics\/sochi-remains-a-work-in-progress-as-games-draw-near.html":{"count":99,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/04\/sports\/olympics\/sochi-remains-a-work-in-progress-as-games-draw-near.html"},"http:\/\/www.nytimes.com\/2014\/02\/04\/sports\/soccer\/a-souvenir-and-a-memory.html":{"count":0,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/04\/sports\/soccer\/a-souvenir-and-a-memory.html"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/02\/02\/in-adoption-does-race-matter\/adoptions-should-consider-black-children-and-black-families":{"count":12,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/02\/02\/in-adoption-does-race-matter\/adoptions-should-consider-black-children-and-black-families"},"http:\/\/www.nytimes.com\/2014\/02\/03\/world\/europe\/as-ukraines-president-returns-from-leave-his-options-seem-dismal.html":{"count":14,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/03\/world\/europe\/as-ukraines-president-returns-from-leave-his-options-seem-dismal.html"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/02\/02\/in-adoption-does-race-matter\/in-adoption-placements-no-room-for-racism":{"count":0,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/02\/02\/in-adoption-does-race-matter\/in-adoption-placements-no-room-for-racism"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/02\/02\/in-adoption-does-race-matter\/in-adoptions-take-race-out-of-the-equation":{"count":15,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/02\/02\/in-adoption-does-race-matter\/in-adoptions-take-race-out-of-the-equation"},"http:\/\/www.nytimes.com\/2014\/02\/04\/sports\/football\/after-doing-it-their-way-seahawks-savor-the-moment.html":{"count":97,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/04\/sports\/football\/after-doing-it-their-way-seahawks-savor-the-moment.html"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/02\/02\/in-adoption-does-race-matter\/in-adoption-some-racial-biases-arent-examined":{"count":58,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/02\/02\/in-adoption-does-race-matter\/in-adoption-some-racial-biases-arent-examined"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/02\/02\/in-adoption-does-race-matter\/in-adoption-race-should-not-be-ignored":{"count":65,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/02\/02\/in-adoption-does-race-matter\/in-adoption-race-should-not-be-ignored"},"http:\/\/www.nytimes.com\/2014\/02\/03\/health\/effort-to-test-health-policies-is-criticized-for-study-tactics.html":{"count":76,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/03\/health\/effort-to-test-health-policies-is-criticized-for-study-tactics.html"},"http:\/\/www.nytimes.com\/2014\/02\/03\/sports\/football\/peyton-manning-goes-cold-as-seattle-brings-the-heat.html":{"count":176,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/03\/sports\/football\/peyton-manning-goes-cold-as-seattle-brings-the-heat.html"},"http:\/\/www.nytimes.com\/2014\/02\/03\/booming\/enlisting-dad-to-find-a-first-bra.html":{"count":31,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/03\/booming\/enlisting-dad-to-find-a-first-bra.html"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/03\/02\/in-adoption-does-race-matter\/in-adoption-some-racial-biases-arent-examined":{"count":13,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/03\/02\/in-adoption-does-race-matter\/in-adoption-some-racial-biases-arent-examined"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/03\/02\/in-adoption-does-race-matter\/in-adoptions-take-race-out-of-the-equation":{"count":3,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/03\/02\/in-adoption-does-race-matter\/in-adoptions-take-race-out-of-the-equation"},"http:\/\/www.nytimes.com\/2014\/02\/03\/us\/battles-loom-in-many-states-over-what-to-do-with-budget-surpluses.html":{"count":398,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/03\/us\/battles-loom-in-many-states-over-what-to-do-with-budget-surpluses.html"},"http:\/\/www.nytimes.com\/2014\/02\/03\/sports\/football\/start-to-finish-its-all-seahawks.html":{"count":211,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/03\/sports\/football\/start-to-finish-its-all-seahawks.html"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/03\/02\/in-adoption-does-race-matter\/in-adoption-placements-no-room-for-racism":{"count":4,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/03\/02\/in-adoption-does-race-matter\/in-adoption-placements-no-room-for-racism"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/03\/02\/in-adoption-does-race-matter\/adoptions-should-consider-black-children-and-black-families":{"count":1,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/03\/02\/in-adoption-does-race-matter\/adoptions-should-consider-black-children-and-black-families"},"http:\/\/www.nytimes.com\/2014\/02\/03\/opinion\/a-new-way-to-rein-in-fat-cats.html":{"count":228,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/03\/opinion\/a-new-way-to-rein-in-fat-cats.html"},"http:\/\/www.nytimes.com\/2014\/02\/03\/business\/the-middle-class-is-steadily-eroding-just-ask-the-business-world.html":{"count":999,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/03\/business\/the-middle-class-is-steadily-eroding-just-ask-the-business-world.html"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/03\/02\/in-adoption-does-race-matter\/in-adoption-race-should-not-be-ignored":{"count":20,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/03\/02\/in-adoption-does-race-matter\/in-adoption-race-should-not-be-ignored"},"http:\/\/www.nytimes.com\/2014\/02\/03\/opinion\/the-capitols-spinning-door-accelerates.html":{"count":119,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/03\/opinion\/the-capitols-spinning-door-accelerates.html"},"http:\/\/www.nytimes.com\/2014\/02\/03\/business\/newly-wary-shoppers-trust-cash.html":{"count":67,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/03\/business\/newly-wary-shoppers-trust-cash.html"},"http:\/\/www.nytimes.com\/2014\/02\/03\/opinion\/krugman-delusions-of-failure.html":{"count":858,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/03\/opinion\/krugman-delusions-of-failure.html"},"http:\/\/www.nytimes.com\/2014\/02\/03\/opinion\/we-need-gmo-wheat.html":{"count":438,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/03\/opinion\/we-need-gmo-wheat.html"},"http:\/\/www.nytimes.com\/2014\/02\/03\/opinion\/abbass-nato-proposal.html":{"count":212,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/03\/opinion\/abbass-nato-proposal.html"},"http:\/\/www.nytimes.com\/2014\/02\/03\/movies\/philip-seymour-hoffman-actor-dies-at-46.html":{"count":824,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/03\/movies\/philip-seymour-hoffman-actor-dies-at-46.html"},"http:\/\/www.nytimes.com\/2014\/02\/02\/magazine\/theres-a-reason-that-rye-is-having-a-moment.html":{"count":3,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/02\/magazine\/theres-a-reason-that-rye-is-having-a-moment.html"},"http:\/\/www.nytimes.com\/2014\/02\/02\/us\/politics\/glitches-in-state-exchanges-give-gop-a-cudgel.html":{"count":221,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/02\/us\/politics\/glitches-in-state-exchanges-give-gop-a-cudgel.html"},"http:\/\/movies.nytimes.com\/movie\/104012\/Night-Unto-Night\/overview":{"count":0,"commentsEnabled":true,"assetUrl":"http:\/\/movies.nytimes.com\/movie\/104012\/Night-Unto-Night\/overview"},"http:\/\/www.nytimes.com\/2014\/02\/02\/nyregion\/a-mayor-most-everybody-looks-up-to-even-when-he-slouches.html":{"count":117,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/02\/nyregion\/a-mayor-most-everybody-looks-up-to-even-when-he-slouches.html"},"http:\/\/movies.nytimes.com\/movie\/466490\/Papirosen\/overview":{"count":0,"commentsEnabled":true,"assetUrl":"http:\/\/movies.nytimes.com\/movie\/466490\/Papirosen\/overview"},"http:\/\/www.nytimes.com\/2014\/02\/01\/opinion\/sunday\/are-you-my-cousin.html":{"count":131,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/01\/opinion\/sunday\/are-you-my-cousin.html"},"http:\/\/www.nytimes.com\/2014\/02\/02\/opinion\/sunday\/what-gop-style-reform-looks-like.html":{"count":430,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/02\/opinion\/sunday\/what-gop-style-reform-looks-like.html"},"http:\/\/www.nytimes.com\/2014\/02\/02\/opinion\/sunday\/friedman-a-wonderful-country.html":{"count":135,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/02\/opinion\/sunday\/friedman-a-wonderful-country.html"},"http:\/\/www.nytimes.com\/2014\/02\/02\/sports\/football\/denvers-offense-unstoppable-vs-seattles-defense-unmovable.html":{"count":32,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/02\/sports\/football\/denvers-offense-unstoppable-vs-seattles-defense-unmovable.html"},"http:\/\/www.nytimes.com\/2014\/02\/02\/sports\/olympics\/a-swift-and-fatal-luge-plunge-and-then-an-abyss-of-sorrow.html":{"count":58,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/02\/sports\/olympics\/a-swift-and-fatal-luge-plunge-and-then-an-abyss-of-sorrow.html"},"http:\/\/www.nytimes.com\/2014\/02\/02\/opinion\/sunday\/douthat-the-gops-immigration-delusion.html":{"count":197,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/02\/opinion\/sunday\/douthat-the-gops-immigration-delusion.html"},"http:\/\/www.nytimes.com\/2014\/02\/02\/opinion\/sunday\/dowd-the-gospel-according-to-paul.html":{"count":660,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/02\/opinion\/sunday\/dowd-the-gospel-according-to-paul.html"},"http:\/\/movies.nytimes.com\/movie\/148219\/Victory-Through-Air-Power\/overview":{"count":1,"commentsEnabled":true,"assetUrl":"http:\/\/movies.nytimes.com\/movie\/148219\/Victory-Through-Air-Power\/overview"},"http:\/\/www.nytimes.com\/2014\/02\/02\/sports\/football\/hes-pete-carrolls-guardian-tweeter.html":{"count":3,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/02\/sports\/football\/hes-pete-carrolls-guardian-tweeter.html"},"http:\/\/www.nytimes.com\/2014\/02\/02\/nyregion\/when-owning-a-home-is-cold-comfort.html":{"count":36,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/02\/nyregion\/when-owning-a-home-is-cold-comfort.html"},"http:\/\/www.nytimes.com\/2014\/02\/02\/opinion\/sunday\/bruni-maturitys-victories.html":{"count":124,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/02\/opinion\/sunday\/bruni-maturitys-victories.html"},"http:\/\/www.nytimes.com\/2014\/01\/31\/booming\/with-persistence-he-caught-the-girl-next-door.html":{"count":12,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/31\/booming\/with-persistence-he-caught-the-girl-next-door.html"},"http:\/\/www.nytimes.com\/2014\/02\/01\/business\/when-retirement-seems-impossible-or-just-boring.html":{"count":231,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/01\/business\/when-retirement-seems-impossible-or-just-boring.html"},"http:\/\/www.nytimes.com\/2014\/02\/01\/sports\/football\/paul-allen-the-seahawks-man-in-the-shadows-shows-them-the-light.html":{"count":14,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/01\/sports\/football\/paul-allen-the-seahawks-man-in-the-shadows-shows-them-the-light.html"},"http:\/\/www.nytimes.com\/2014\/02\/02\/nyregion\/lone-fan-tackles-the-nfl-over-super-bowl-ticket-prices.html":{"count":128,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/02\/nyregion\/lone-fan-tackles-the-nfl-over-super-bowl-ticket-prices.html"},"http:\/\/www.nytimes.com\/2014\/02\/01\/opinion\/costa-ricas-wrong-turn.html":{"count":22,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/01\/opinion\/costa-ricas-wrong-turn.html"},"http:\/\/www.nytimes.com\/2014\/02\/01\/world\/middleeast\/turkey.html":{"count":31,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/01\/world\/middleeast\/turkey.html"},"http:\/\/www.nytimes.com\/2014\/02\/01\/sports\/football\/for-the-colquitt-punters-4th-down-is-family-time.html":{"count":13,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/01\/sports\/football\/for-the-colquitt-punters-4th-down-is-family-time.html"},"http:\/\/www.nytimes.com\/2014\/02\/01\/your-money\/need-tax-help-irs-may-not-be-the-best-place-to-go.html":{"count":3,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/01\/your-money\/need-tax-help-irs-may-not-be-the-best-place-to-go.html"},"http:\/\/www.nytimes.com\/2014\/02\/01\/sports\/soccer\/as-manchester-united-flails-its-chosen-manager-feels-the-strain.html":{"count":9,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/01\/sports\/soccer\/as-manchester-united-flails-its-chosen-manager-feels-the-strain.html"},"http:\/\/www.nytimes.com\/2014\/02\/01\/opinion\/the-masculine-mistake.html":{"count":287,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/01\/opinion\/the-masculine-mistake.html"},"http:\/\/www.nytimes.com\/2014\/02\/01\/opinion\/the-economic-road-ahead.html":{"count":176,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/01\/opinion\/the-economic-road-ahead.html"},"http:\/\/www.nytimes.com\/2014\/02\/01\/opinion\/the-super-bowl-of-sex-trafficking.html":{"count":117,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/01\/opinion\/the-super-bowl-of-sex-trafficking.html"},"http:\/\/www.nytimes.com\/2014\/02\/01\/sports\/football\/too-loud-too-quiet-those-alluring-seahawks.html":{"count":8,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/01\/sports\/football\/too-loud-too-quiet-those-alluring-seahawks.html"},"http:\/\/www.nytimes.com\/2014\/02\/01\/opinion\/nocera-unionized-college-athletes.html":{"count":90,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/01\/opinion\/nocera-unionized-college-athletes.html"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/31\/the-stakes-off-the-field-and-at-the-betting-window\/sports-betting-is-a-thrill-let-people-enjoy-it":{"count":7,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/31\/the-stakes-off-the-field-and-at-the-betting-window\/sports-betting-is-a-thrill-let-people-enjoy-it"},"http:\/\/www.nytimes.com\/2014\/02\/01\/opinion\/collins-christie-plays-defense.html":{"count":260,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/01\/opinion\/collins-christie-plays-defense.html"},"http:\/\/www.nytimes.com\/2014\/02\/02\/fashion\/good-enough-thats-great.html":{"count":126,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/02\/fashion\/good-enough-thats-great.html"},"http:\/\/www.nytimes.com\/2014\/02\/01\/us\/snacks-laced-with-marijuana-raise-concerns.html":{"count":422,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/01\/us\/snacks-laced-with-marijuana-raise-concerns.html"},"http:\/\/www.nytimes.com\/2014\/02\/01\/your-money\/with-engagement-rings-love-meets-budget.html":{"count":100,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/01\/your-money\/with-engagement-rings-love-meets-budget.html"},"http:\/\/www.nytimes.com\/2014\/02\/01\/us\/influx-of-snowy-owls-thrills-and-baffles-birders.html":{"count":79,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/01\/us\/influx-of-snowy-owls-thrills-and-baffles-birders.html"},"http:\/\/travel.nytimes.com\/2014\/02\/02\/travel\/orhan-pamuks-istanbul.html":{"count":72,"commentsEnabled":false,"assetUrl":"http:\/\/travel.nytimes.com\/2014\/02\/02\/travel\/orhan-pamuks-istanbul.html"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/31\/the-stakes-off-the-field-and-at-the-betting-window\/legalized-sports-betting-would-threaten-sports-and-society":{"count":5,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/31\/the-stakes-off-the-field-and-at-the-betting-window\/legalized-sports-betting-would-threaten-sports-and-society"},"http:\/\/www.nytimes.com\/2014\/02\/05\/dining\/get-them-while-theyre-green.html":{"count":5,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/05\/dining\/get-them-while-theyre-green.html"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/31\/the-stakes-off-the-field-and-at-the-betting-window\/government-bookies-feed-inequality":{"count":4,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/31\/the-stakes-off-the-field-and-at-the-betting-window\/government-bookies-feed-inequality"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/31\/the-stakes-off-the-field-and-at-the-betting-window\/stop-the-hypocrisy-about-sports-betting":{"count":3,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/31\/the-stakes-off-the-field-and-at-the-betting-window\/stop-the-hypocrisy-about-sports-betting"},"http:\/\/www.nytimes.com\/news\/minute\/2014\/01\/31\/times-minute-tray-tables-up\/":{"count":1,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/news\/minute\/2014\/01\/31\/times-minute-tray-tables-up\/"},"http:\/\/www.nytimes.com\/2014\/02\/01\/nyregion\/christie-bridge.html":{"count":1260,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/01\/nyregion\/christie-bridge.html"},"http:\/\/www.nytimes.com\/2014\/02\/05\/sports\/olympics\/in-russia-skating-booms-again.html":{"count":1,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/05\/sports\/olympics\/in-russia-skating-booms-again.html"},"http:\/\/www.nytimes.com\/2014\/02\/01\/sports\/olympics\/winter-olympians-to-follow-on-instagram.html":{"count":0,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/01\/sports\/olympics\/winter-olympians-to-follow-on-instagram.html"},"http:\/\/www.nytimes.com\/2014\/02\/01\/us\/politics\/report-may-ease-way-to-approval-of-keystone-pipeline.html":{"count":711,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/01\/us\/politics\/report-may-ease-way-to-approval-of-keystone-pipeline.html"},"http:\/\/www.nytimes.com\/2014\/02\/02\/magazine\/grown-up-clothes.html":{"count":7,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/02\/magazine\/grown-up-clothes.html"},"http:\/\/www.nytimes.com\/2014\/02\/05\/dining\/with-california-syrahs-an-asian-accented-chili.html":{"count":2,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/05\/dining\/with-california-syrahs-an-asian-accented-chili.html"},"http:\/\/www.nytimes.com\/2014\/02\/02\/realestate\/when-the-prescription-is-fresh-air.html":{"count":3,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/02\/realestate\/when-the-prescription-is-fresh-air.html"},"http:\/\/www.nytimes.com\/2014\/02\/02\/magazine\/our-young-adult-dystopia.html":{"count":14,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/02\/magazine\/our-young-adult-dystopia.html"},"http:\/\/www.nytimes.com\/2014\/02\/01\/business\/accounting-for-jamie-dimons-big-pay-raise.html":{"count":388,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/01\/business\/accounting-for-jamie-dimons-big-pay-raise.html"},"http:\/\/www.nytimes.com\/roomfordebate\/2013\/09\/18\/reconsidering-young-lifers-sentences\/the-problem-with-retroactivity-rules":{"count":1,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2013\/09\/18\/reconsidering-young-lifers-sentences\/the-problem-with-retroactivity-rules"},"http:\/\/www.nytimes.com\/2014\/02\/02\/realestate\/the-truly-affordable-new-york-apartment.html":{"count":138,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/02\/realestate\/the-truly-affordable-new-york-apartment.html"},"http:\/\/www.nytimes.com\/2014\/02\/02\/magazine\/who-made-that-first-person-shooter-game.html":{"count":6,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/02\/magazine\/who-made-that-first-person-shooter-game.html"},"http:\/\/www.nytimes.com\/2014\/02\/01\/us\/politics\/big-companies-join-obama-in-initiative-to-help-long-term-unemployed.html":{"count":179,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/01\/us\/politics\/big-companies-join-obama-in-initiative-to-help-long-term-unemployed.html"},"http:\/\/www.nytimes.com\/2014\/02\/01\/us\/obama-hints-he-may-be-open-to-immigration-deal-with-gop.html":{"count":173,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/01\/us\/obama-hints-he-may-be-open-to-immigration-deal-with-gop.html"},"http:\/\/www.nytimes.com\/2014\/02\/02\/magazine\/get-out-of-my-subconscious.html":{"count":36,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/02\/magazine\/get-out-of-my-subconscious.html"},"http:\/\/www.nytimes.com\/2014\/02\/02\/magazine\/the-post-hope-politics-of-house-of-cards.html":{"count":25,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/02\/magazine\/the-post-hope-politics-of-house-of-cards.html"},"http:\/\/www.nytimes.com\/2014\/02\/02\/magazine\/elaine-strich-broadway-legend-entertaining-is-hard.html":{"count":11,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/02\/magazine\/elaine-strich-broadway-legend-entertaining-is-hard.html"},"http:\/\/www.nytimes.com\/2014\/01\/31\/booming\/knocking-once-again-on-the-poets-door.html":{"count":10,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/31\/booming\/knocking-once-again-on-the-poets-door.html"},"http:\/\/www.nytimes.com\/2014\/02\/01\/nyregion\/bratton-tells-chiefs-hell-stop-sending-rookies-to-high-crime-areas.html":{"count":125,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/01\/nyregion\/bratton-tells-chiefs-hell-stop-sending-rookies-to-high-crime-areas.html"},"http:\/\/www.nytimes.com\/2014\/01\/31\/us\/politics\/in-landrieu-races-obama-helps-and-hinders.html":{"count":25,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/31\/us\/politics\/in-landrieu-races-obama-helps-and-hinders.html"},"http:\/\/www.nytimes.com\/2014\/01\/31\/sports\/soccer\/riding-a-van-to-soccer-practice-with-a-world-cup-starter-at-the-wheel.html":{"count":9,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/31\/sports\/soccer\/riding-a-van-to-soccer-practice-with-a-world-cup-starter-at-the-wheel.html"},"http:\/\/www.nytimes.com\/2014\/01\/31\/nyregion\/trademark-trumps-charity-so-us-will-destroy-bogus-nfl-jerseys.html":{"count":11,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/31\/nyregion\/trademark-trumps-charity-so-us-will-destroy-bogus-nfl-jerseys.html"},"http:\/\/movies.nytimes.com\/movie\/462526\/Caf-de-Flore\/overview":{"count":0,"commentsEnabled":true,"assetUrl":"http:\/\/movies.nytimes.com\/movie\/462526\/Caf-de-Flore\/overview"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/30\/when-visa-holders-behave-badly-in-the-us\/when-visa-holders-behave-badly-in-the-us-response-57":{"count":18,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/30\/when-visa-holders-behave-badly-in-the-us\/when-visa-holders-behave-badly-in-the-us-response-57"},"http:\/\/www.nytimes.com\/2014\/01\/31\/world\/europe\/need-the-best-for-your-next-occasion-call-westminster-palace.html":{"count":3,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/31\/world\/europe\/need-the-best-for-your-next-occasion-call-westminster-palace.html"},"http:\/\/movies.nytimes.com\/movie\/465878\/Somewhere-Slow\/overview":{"count":0,"commentsEnabled":true,"assetUrl":"http:\/\/movies.nytimes.com\/movie\/465878\/Somewhere-Slow\/overview"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/30\/when-visa-holders-behave-badly-in-the-us\/an-extraodinary-case-that-highlights-the-plight-of-the-average-immigrant":{"count":16,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/30\/when-visa-holders-behave-badly-in-the-us\/an-extraodinary-case-that-highlights-the-plight-of-the-average-immigrant"},"http:\/\/www.nytimes.com\/2014\/01\/31\/opinion\/we-are-giving-ourselves-cancer.html":{"count":247,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/31\/opinion\/we-are-giving-ourselves-cancer.html"},"http:\/\/www.nytimes.com\/2014\/01\/31\/opinion\/bernanke-should-be-thanked.html":{"count":125,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/31\/opinion\/bernanke-should-be-thanked.html"},"http:\/\/www.nytimes.com\/2014\/01\/31\/opinion\/cohen-a-middle-eastern-primer.html":{"count":144,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/31\/opinion\/cohen-a-middle-eastern-primer.html"},"http:\/\/www.nytimes.com\/2014\/01\/31\/opinion\/brooks-the-opportunity-coalition.html":{"count":321,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/31\/opinion\/brooks-the-opportunity-coalition.html"},"http:\/\/www.nytimes.com\/2014\/01\/31\/opinion\/krugman-talking-troubled-turkey.html":{"count":321,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/31\/opinion\/krugman-talking-troubled-turkey.html"},"http:\/\/www.nytimes.com\/2014\/01\/31\/opinion\/fixing-immigration-in-principle.html":{"count":213,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/31\/opinion\/fixing-immigration-in-principle.html"},"http:\/\/www.nytimes.com\/2014\/01\/31\/opinion\/second-class-noncitizens.html":{"count":126,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/31\/opinion\/second-class-noncitizens.html"},"http:\/\/theater.nytimes.com\/show\/141158\/The-Bridges-of-Madison-County\/overview":{"count":1,"commentsEnabled":true,"assetUrl":"http:\/\/theater.nytimes.com\/show\/141158\/The-Bridges-of-Madison-County\/overview"},"http:\/\/www.nytimes.com\/2014\/01\/31\/health\/responding-to-critics-gynecology-board-reverses-ban-on-treating-male-patients.html":{"count":44,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/31\/health\/responding-to-critics-gynecology-board-reverses-ban-on-treating-male-patients.html"},"http:\/\/www.nytimes.com\/2014\/01\/31\/world\/middleeast\/its-great-lake-shriveled-iran-confronts-crisis-of-water-supply.html":{"count":188,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/31\/world\/middleeast\/its-great-lake-shriveled-iran-confronts-crisis-of-water-supply.html"},"http:\/\/www.nytimes.com\/2014\/01\/31\/opinion\/egan-when-biography-trumps-substance.html":{"count":573,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/31\/opinion\/egan-when-biography-trumps-substance.html"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/30\/when-visa-holders-behave-badly-in-the-us\/revoke-biebers-visa":{"count":230,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/30\/when-visa-holders-behave-badly-in-the-us\/revoke-biebers-visa"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/30\/when-visa-holders-behave-badly-in-the-us\/lax-deportation-patterns-will-keep-bieber-types-safe":{"count":47,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/30\/when-visa-holders-behave-badly-in-the-us\/lax-deportation-patterns-will-keep-bieber-types-safe"},"http:\/\/www.nytimes.com\/2014\/01\/31\/nyregion\/super-bowl-fever-hits-midtown-but-not-everyone-has-caught-it.html":{"count":49,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/31\/nyregion\/super-bowl-fever-hits-midtown-but-not-everyone-has-caught-it.html"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/30\/when-visa-holders-behave-badly-in-the-us\/the-costs-of-deportation-are-too-high-already":{"count":45,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/30\/when-visa-holders-behave-badly-in-the-us\/the-costs-of-deportation-are-too-high-already"},"http:\/\/www.nytimes.com\/2014\/01\/31\/world\/vice-admiral-to-be-named-nsa-director.html":{"count":76,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/31\/world\/vice-admiral-to-be-named-nsa-director.html"},"http:\/\/www.nytimes.com\/news\/minute\/2014\/01\/30\/times-minute-ads-that-track-you\/":{"count":2,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/news\/minute\/2014\/01\/30\/times-minute-ads-that-track-you\/"},"http:\/\/www.nytimes.com\/2014\/02\/05\/dining\/california-syrahs-on-such-a-winters-day.html":{"count":21,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/05\/dining\/california-syrahs-on-such-a-winters-day.html"},"http:\/\/www.nytimes.com\/2014\/02\/02\/realestate\/why-cant-i-have-a-washing-machine.html":{"count":21,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/02\/realestate\/why-cant-i-have-a-washing-machine.html"},"http:\/\/theater.nytimes.com\/show\/182548\/Beertown\/overview":{"count":0,"commentsEnabled":true,"assetUrl":"http:\/\/theater.nytimes.com\/show\/182548\/Beertown\/overview"},"http:\/\/www.nytimes.com\/2014\/01\/31\/dining\/husband-and-wife-chefs-split-from-calliope.html":{"count":4,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/31\/dining\/husband-and-wife-chefs-split-from-calliope.html"},"http:\/\/www.nytimes.com\/2014\/02\/02\/magazine\/the-super-bowl-of-sports-gambling.html":{"count":12,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/02\/magazine\/the-super-bowl-of-sports-gambling.html"},"http:\/\/www.nytimes.com\/2014\/01\/31\/sports\/football\/shoulder-pads-slim-down-in-faster-sleeker-nfl.html":{"count":13,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/31\/sports\/football\/shoulder-pads-slim-down-in-faster-sleeker-nfl.html"},"http:\/\/travel.nytimes.com\/2014\/02\/02\/travel\/wintertime-bargains-in-budapest.html":{"count":18,"commentsEnabled":false,"assetUrl":"http:\/\/travel.nytimes.com\/2014\/02\/02\/travel\/wintertime-bargains-in-budapest.html"},"http:\/\/www.nytimes.com\/2014\/01\/31\/us\/boston-marathon-bombing-case.html":{"count":364,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/31\/us\/boston-marathon-bombing-case.html"},"http:\/\/www.nytimes.com\/2014\/01\/31\/technology\/For-Super-Bowl-Personalized-Phone-Alerts.html":{"count":33,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/31\/technology\/For-Super-Bowl-Personalized-Phone-Alerts.html"},"http:\/\/www.nytimes.com\/2014\/01\/31\/world\/europe\/ukraine-unrest.html":{"count":64,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/31\/world\/europe\/ukraine-unrest.html"},"http:\/\/www.nytimes.com\/2014\/01\/31\/sports\/football\/inspired-and-already-trying-to-be-the-nfls-next-deaf-player.html":{"count":8,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/31\/sports\/football\/inspired-and-already-trying-to-be-the-nfls-next-deaf-player.html"},"http:\/\/www.nytimes.com\/2014\/01\/31\/nyregion\/de-blasio-stop-and-frisk.html":{"count":312,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/31\/nyregion\/de-blasio-stop-and-frisk.html"},"http:\/\/www.nytimes.com\/2014\/01\/31\/us\/politics\/henry-a-waxman-a-house-democratic-fixture-will-retire.html":{"count":323,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/31\/us\/politics\/henry-a-waxman-a-house-democratic-fixture-will-retire.html"},"http:\/\/www.nytimes.com\/news\/minute\/2014\/01\/30\/times-minute-obesity-and-children\/":{"count":0,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/news\/minute\/2014\/01\/30\/times-minute-obesity-and-children\/"},"http:\/\/www.nytimes.com\/2014\/01\/30\/booming\/trapped-by-als-he-urged-his-daughter-to-fly-free.html":{"count":15,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/30\/booming\/trapped-by-als-he-urged-his-daughter-to-fly-free.html"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/29\/presidential-power-vs-congressional-inertia\/great-executive-orders-by-great-presidents":{"count":9,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/29\/presidential-power-vs-congressional-inertia\/great-executive-orders-by-great-presidents"},"http:\/\/www.nytimes.com\/2014\/01\/30\/nyregion\/powerful-allies-pushed-a-project-in-new-jersey.html":{"count":176,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/30\/nyregion\/powerful-allies-pushed-a-project-in-new-jersey.html"},"http:\/\/www.nytimes.com\/2014\/01\/30\/garden\/sometimes-asparagus-is-more-than-asparagus.html":{"count":15,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/30\/garden\/sometimes-asparagus-is-more-than-asparagus.html"},"http:\/\/www.nytimes.com\/2014\/01\/30\/world\/europe\/beneath-southern-italy-a-deadly-mob-legacy.html":{"count":124,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/30\/world\/europe\/beneath-southern-italy-a-deadly-mob-legacy.html"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/29\/presidential-power-vs-congressional-inertia\/obamas-executive-orders-will-annoy-friends-and-foes":{"count":5,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/29\/presidential-power-vs-congressional-inertia\/obamas-executive-orders-will-annoy-friends-and-foes"},"http:\/\/www.nytimes.com\/2014\/01\/30\/world\/europe\/us-says-russia-tested-missile-despite-treaty.html":{"count":256,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/30\/world\/europe\/us-says-russia-tested-missile-despite-treaty.html"},"http:\/\/www.nytimes.com\/2014\/01\/30\/sports\/football\/a-pioneering-black-quarterbacks-lasting-legacy.html":{"count":10,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/30\/sports\/football\/a-pioneering-black-quarterbacks-lasting-legacy.html"},"http:\/\/www.nytimes.com\/2014\/01\/29\/booming\/on-losing-it-or-not.html":{"count":15,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/29\/booming\/on-losing-it-or-not.html"},"http:\/\/www.nytimes.com\/2014\/01\/30\/opinion\/blow-the-incredible-shrinking-presidency.html":{"count":503,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/30\/opinion\/blow-the-incredible-shrinking-presidency.html"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/29\/presidential-power-vs-congressional-inertia\/president-obamas-desire-to-wield-executive-power-is-understandable":{"count":10,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/29\/presidential-power-vs-congressional-inertia\/president-obamas-desire-to-wield-executive-power-is-understandable"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/29\/presidential-power-vs-congressional-inertia\/presidents-cannot-ignore-laws-as-written":{"count":57,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/29\/presidential-power-vs-congressional-inertia\/presidents-cannot-ignore-laws-as-written"},"http:\/\/www.nytimes.com\/2014\/01\/30\/sports\/football\/under-nfl-settlement-making-pie-without-knowing-total-slices.html":{"count":62,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/30\/sports\/football\/under-nfl-settlement-making-pie-without-knowing-total-slices.html"},"http:\/\/www.nytimes.com\/2014\/01\/30\/sports\/football\/russell-wilson-is-a-standout-whos-easy-to-miss.html":{"count":52,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/30\/sports\/football\/russell-wilson-is-a-standout-whos-easy-to-miss.html"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/29\/presidential-power-vs-congressional-inertia\/executive-authority-is-a-powerful-tool-to-use-with-caution":{"count":20,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/29\/presidential-power-vs-congressional-inertia\/executive-authority-is-a-powerful-tool-to-use-with-caution"},"http:\/\/www.nytimes.com\/2014\/01\/30\/nyregion\/after-keeping-company-with-mobsters-a-politician-now-speaks-their-language.html":{"count":44,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/30\/nyregion\/after-keeping-company-with-mobsters-a-politician-now-speaks-their-language.html"},"http:\/\/www.nytimes.com\/2014\/01\/30\/opinion\/collins-how-preschool-got-hot.html":{"count":246,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/30\/opinion\/collins-how-preschool-got-hot.html"},"http:\/\/www.nytimes.com\/2014\/01\/30\/opinion\/secrecy-behind-executions.html":{"count":189,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/30\/opinion\/secrecy-behind-executions.html"},"http:\/\/www.nytimes.com\/2014\/01\/30\/opinion\/how-to-get-more-early-bloomers.html":{"count":99,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/30\/opinion\/how-to-get-more-early-bloomers.html"},"http:\/\/www.nytimes.com\/2014\/01\/30\/opinion\/kristof-pre-k-the-great-debate.html":{"count":197,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/30\/opinion\/kristof-pre-k-the-great-debate.html"},"http:\/\/www.nytimes.com\/2014\/01\/30\/nyregion\/a-winged-symbol-of-love-that-new-york-state-wants-banished.html":{"count":119,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/30\/nyregion\/a-winged-symbol-of-love-that-new-york-state-wants-banished.html"},"http:\/\/www.nytimes.com\/news\/minute\/2014\/01\/29\/times-minute-secrets-of-successful-aging\/":{"count":2,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/news\/minute\/2014\/01\/29\/times-minute-secrets-of-successful-aging\/"},"http:\/\/www.nytimes.com\/news\/minute\/2014\/01\/29\/times-minute-grimm-threat\/":{"count":3,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/news\/minute\/2014\/01\/29\/times-minute-grimm-threat\/"},"http:\/\/www.nytimes.com\/2014\/01\/30\/science\/obesity-takes-hold-early-in-life-study-finds.html":{"count":380,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/30\/science\/obesity-takes-hold-early-in-life-study-finds.html"},"http:\/\/www.nytimes.com\/restaurants\/1248069043718\/the-cecil\/details.html":{"count":0,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/restaurants\/1248069043718\/the-cecil\/details.html"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/29\/why-is-latin-america-so-progressive-on-gay-rights\/in-latin-america-human-rights-causes-resonate":{"count":2,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/29\/why-is-latin-america-so-progressive-on-gay-rights\/in-latin-america-human-rights-causes-resonate"},"http:\/\/tv.nytimes.com\/show\/207675\/Gas-Land\/overview":{"count":0,"commentsEnabled":true,"assetUrl":"http:\/\/tv.nytimes.com\/show\/207675\/Gas-Land\/overview"},"http:\/\/www.nytimes.com\/2014\/01\/30\/business\/media\/as-i-was-saying-about-web-journalism-a-bubble-or-a-lasting-business.html":{"count":5,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/30\/business\/media\/as-i-was-saying-about-web-journalism-a-bubble-or-a-lasting-business.html"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/29\/why-is-latin-america-so-progressive-on-gay-rights\/javier-corrales-noon-tues":{"count":1,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/29\/why-is-latin-america-so-progressive-on-gay-rights\/javier-corrales-noon-tues"},"http:\/\/www.nytimes.com\/2014\/01\/30\/us\/politics\/democrats-look-to-tie-gop-senate-candidates-to-unpopular-house.html":{"count":210,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/30\/us\/politics\/democrats-look-to-tie-gop-senate-candidates-to-unpopular-house.html"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/29\/why-is-latin-america-so-progressive-on-gay-rights\/in-brazil-aids-activism-led-to-political-connections":{"count":1,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/29\/why-is-latin-america-so-progressive-on-gay-rights\/in-brazil-aids-activism-led-to-political-connections"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/29\/why-is-latin-america-so-progressive-on-gay-rights\/why-latin-american-courts-favor-gay-rights":{"count":17,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/29\/why-is-latin-america-so-progressive-on-gay-rights\/why-latin-american-courts-favor-gay-rights"},"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/29\/why-is-latin-america-so-progressive-on-gay-rights\/homophobia-in-the-caribbean":{"count":6,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/roomfordebate\/2014\/01\/29\/why-is-latin-america-so-progressive-on-gay-rights\/homophobia-in-the-caribbean"},"http:\/\/www.nytimes.com\/2014\/01\/30\/us\/texas-democrat-defends-back-story-under-criticism.html":{"count":496,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/30\/us\/texas-democrat-defends-back-story-under-criticism.html"},"http:\/\/www.nytimes.com\/2014\/01\/30\/nyregion\/rep-michael-grimm-threat-ny1-reporter.html":{"count":606,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/30\/nyregion\/rep-michael-grimm-threat-ny1-reporter.html"},"http:\/\/www.nytimes.com\/2014\/02\/02\/magazine\/just-when-you-thought-quinoa-couldnt-be-crunchier.html":{"count":24,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/02\/magazine\/just-when-you-thought-quinoa-couldnt-be-crunchier.html"},"http:\/\/www.nytimes.com\/2014\/01\/30\/us\/ice-storm-southern-united-states.html":{"count":578,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/30\/us\/ice-storm-southern-united-states.html"},"http:\/\/www.nytimes.com\/2014\/01\/29\/dining\/fine-tempura-piece-by-delectable-piece.html":{"count":11,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/29\/dining\/fine-tempura-piece-by-delectable-piece.html"},"http:\/\/www.nytimes.com\/2014\/01\/29\/us\/frigid-blast-disrupts-life-in-south-and-midwest-as-emergencies-are-declared.html":{"count":3,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/29\/us\/frigid-blast-disrupts-life-in-south-and-midwest-as-emergencies-are-declared.html"},"http:\/\/www.nytimes.com\/2014\/01\/29\/sports\/olympics\/devry-becomes-an-unlikely-olympic-powerhouse.html":{"count":5,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/29\/sports\/olympics\/devry-becomes-an-unlikely-olympic-powerhouse.html"},"http:\/\/www.nytimes.com\/2014\/02\/02\/magazine\/confessions-of-a-tiger-couple.html":{"count":370,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/02\/02\/magazine\/confessions-of-a-tiger-couple.html"},"http:\/\/www.nytimes.com\/2014\/01\/29\/us\/military-is-asked-to-return-guantanamo-inmate-to-yemen.html":{"count":13,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/29\/us\/military-is-asked-to-return-guantanamo-inmate-to-yemen.html"},"http:\/\/www.nytimes.com\/2014\/01\/29\/booming\/fido-prefers-organic.html":{"count":21,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/29\/booming\/fido-prefers-organic.html"},"http:\/\/www.nytimes.com\/2014\/01\/29\/world\/middleeast\/rebels-in-syria-claim-control-of-resources.html":{"count":34,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/29\/world\/middleeast\/rebels-in-syria-claim-control-of-resources.html"},"http:\/\/www.nytimes.com\/2014\/01\/29\/nyregion\/for-christie-politics-team-kept-a-focus-on-two-bids.html":{"count":200,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/29\/nyregion\/for-christie-politics-team-kept-a-focus-on-two-bids.html"},"http:\/\/www.nytimes.com\/2014\/01\/29\/business\/international\/in-france-a-battle-to-keep-menus-fresh.html":{"count":34,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/29\/business\/international\/in-france-a-battle-to-keep-menus-fresh.html"},"http:\/\/www.nytimes.com\/2014\/01\/29\/sports\/football\/football-fans-do-not-forget-its-new-jersey.html":{"count":87,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/29\/sports\/football\/football-fans-do-not-forget-its-new-jersey.html"},"http:\/\/www.nytimes.com\/2014\/01\/29\/business\/international\/frozen-foie-gras-quelle-horreur.html":{"count":3,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/29\/business\/international\/frozen-foie-gras-quelle-horreur.html"},"http:\/\/www.nytimes.com\/2014\/01\/29\/arts\/video-games\/capturing-footballs-snaps-crackles-and-pops-in-madden-nfl.html":{"count":3,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/29\/arts\/video-games\/capturing-footballs-snaps-crackles-and-pops-in-madden-nfl.html"},"http:\/\/www.nytimes.com\/2014\/01\/29\/us\/politics\/executive-order-may-be-only-option-but-it-comes-with-limits.html":{"count":506,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/29\/us\/politics\/executive-order-may-be-only-option-but-it-comes-with-limits.html"},"http:\/\/www.nytimes.com\/2014\/01\/29\/dining\/protein-bars.html":{"count":39,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/29\/dining\/protein-bars.html"},"http:\/\/www.nytimes.com\/2014\/01\/29\/dining\/restaurant-review-m-wells-steakhouse-in-long-island-city-queens.html":{"count":12,"commentsEnabled":true,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/29\/dining\/restaurant-review-m-wells-steakhouse-in-long-island-city-queens.html"},"http:\/\/www.nytimes.com\/2014\/01\/29\/opinion\/im-looking-through-you.html":{"count":303,"commentsEnabled":false,"assetUrl":"http:\/\/www.nytimes.com\/2014\/01\/29\/opinion\/im-looking-through-you.html"}}</script>		
<IMG CLASS="hidden" SRC="/adx/bin/clientside/4973632cQ2F888888)8)Q7BQ2A7Q2BQ5DQ5DTx88888888)TM88UQ2Bex88e7)Me)xQ2BT" height="1" width="3">






<script type="text/javascript" src="http://js.nyt.com/js2/build/homepage/bottom.js"></script>

			
		<!-- Start UPT call -->
		<img height="1" width="3" border=0 src="http://up.nytimes.com/?d=0/1/&t=1&s=0&ui=&r=&u=www%2enytimes%2ecom%2f%3f">
		<!-- End UPT call -->
	
		
        <script language="JavaScript"><!--
          var dcsvid="";
          var regstatus="non-registered";
        //--></script>
        <script src="http://graphics8.nytimes.com/js/app/analytics/trackingTags_v1.1.js" type="text/javascript"></script>
        <noscript>
          <div><img alt="DCSIMG" id="DCSIMG" width="1" height="1" src="http://wt.o.nytimes.com/dcsym57yw10000s1s8g0boozt_9t1x/njs.gif?dcsuri=/nojavascript&amp;WT.js=No&amp;WT.tv=1.0.7"/></div>
        </noscript>
   
</body>
</html>"""
