import pytest
from bs4 import BeautifulSoup


@pytest.fixture
def search_result_soup():
    html_code = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
            <script type="text/javascript">
                !function () { var e = function () { var e, t = "__tcfapiLocator", a = [], n = window; for (; n;) { try { if (n.frames[t]) { e = n; break } } catch (e) { } if (n === window.top) break; n = n.parent } e || (!function e() { var a = n.document, r = !!n.frames[t]; if (!r) if (a.body) { var i = a.createElement("iframe"); i.style.cssText = "display:none", i.name = t, a.body.appendChild(i) } else setTimeout(e, 5); return !r }(), n.__tcfapi = function () { for (var e, t = arguments.length, n = new Array(t), r = 0; r < t; r++)n[r] = arguments[r]; if (!n.length) return a; if ("setGdprApplies" === n[0]) n.length > 3 && 2 === parseInt(n[1], 10) && "boolean" == typeof n[3] && (e = n[3], "function" == typeof n[2] && n[2]("set", !0)); else if ("ping" === n[0]) { var i = { gdprApplies: e, cmpLoaded: !1, cmpStatus: "stub" }; "function" == typeof n[2] && n[2](i) } else a.push(n) }, n.addEventListener("message", (function (e) { var t = "string" == typeof e.data, a = {}; try { a = t ? JSON.parse(e.data) : e.data } catch (e) { } var n = a.__tcfapiCall; n && window.__tcfapi(n.command, n.version, (function (a, r) { var i = { __tcfapiReturn: { returnValue: a, success: r, callId: n.callId } }; t && (i = JSON.stringify(i)), e.source.postMessage(i, "*") }), n.parameter) }), !1)) }; "undefined" != typeof module ? module.exports = e : e() }();
            </script>
            <script>
            window._sp_ = {
                config: {"accountId":1254,"propertyId":7426,"gdpr":{"consentLanguage":"en"},"baseEndpoint":"https://cdn.privacy-mgmt.com"}}
            </script>
            <script async="" src="https://cdn.privacy-mgmt.com/wrapperMessagingWithoutDetection.js"></script>
            <meta charset="utf-8"/>
            <link href="/favicon.ico" rel="shortcut icon" type="image/x-icon"/>
            <link href="/favicon-16x16.png" rel="shortcut icon" sizes="16x16"/>
            <link href="/android-chrome-192x192.png" rel="shortcut icon" sizes="192x192"/>
            <meta content="width=device-width, initial-scale=1.0, maximum-scale=2.0, user-scalable=no" name="viewport"/>
            <meta content="noindex, nofollow" name="robots"/>
            <meta content="Das ist die Seite der Schnellsuche auf der die Suchergebnisse aus dem Suchfeld anhand des Suchbegriffes angezeigt werden." name="description"/>
            <meta content="article" property="og:type"/>
            <meta content="https://tmssl.akamaized.net/images/tm_logo.png" property="og:image"/>
            <meta content="" property="og:description"/>
            <meta content="Search result" property="og:title"/>
            <meta content="https://www.transfermarkt.co.uk/schnellsuche/ergebnis/schnellsuche?query=Thomas%20Muller&amp;x=0&amp;y=0" property="og:url"/>
            <title>Search result | Transfermarkt</title>
            <div class="werbung werbung-header"><!-- Start GPT Tag -->
            <script src="https://lngtd.com/transfermarkt_ros.js"></script>
            <!-- End GPT Tag --></div> </link></link></head>
            <body class="" data-cmp-layer-id="225254" data-tm-tld="uk" itemscope="" itemtype="http://schema.org/WebPage">
            <div id="main">
            <div class="werbung-skyscraper-container">
            <div class="werbung werbung-skyscraper"><!-- /22272936144,58778164/display_thirdparty/transfermarkt_uk/ros/skyscraper -->
            <div id="div-gpt-ad-skyscrape" style="min-width: 160px; min-height: 600px;"></div>
            <!-- End AdSlot 1 --></div> </div>
            <div class="werbung-skyscraperbtf-container">
            </div>
            <header class="tm-header">
            <div class="tm-header__box">
            <a href="/">
            <img alt="Transfermarkt" class="icon-logo" height="62" src="https://tmsi.akamaized.net/head/transfermarkt_logo.svg" title="Transfermarkt" width="156"/>
            </a>
            <tm-domainswitcher open-list="false" tld="co.uk"></tm-domainswitcher>
            <div class="tm-header__social-box">
            <a class="header__social-link" href="https://www.facebook.com/transfermarkt.co.uk" onclick="tmEvent('SM-Icons_Header','click','Facebook');
            " target="_blank">
            <img class="header__icon" height="20" src="https://tmsi.akamaized.net/icons/socialMedia/fb_icon_hover.svg" width="20"/>
            </a>
            <a class="header__social-link" href="http://twitter.com/TMuk_news" onclick="tmEvent('SM-Icons_Header','click','Twitter');
            " target="_blank">
            <img class="header__icon" height="20" src="https://tmsi.akamaized.net/icons/socialMedia/twitter_icon_hover.svg" width="20"/>
            </a>
            <a class="header__social-link" href="http://instagram.com/transfermarkt_official" onclick="tmEvent('SM-Icons_Header','click','Instagram');
            " target="_blank">
            <img class="header__icon" height="20" src="https://tmsi.akamaized.net/icons/socialMedia/instagram_icon_hover.svg" width="20"/>
            </a>
            <a class="header__social-link" href="/intern/rssguide" onclick="tmEvent('SM-Icons_Header','click','RSS');
            " target="_blank">
            <img class="header__icon" height="20" src="https://tmsi.akamaized.net/icons/socialMedia/rss_icon_hover.svg" width="20"/>
            </a>
            <a class="header__social-link" href="https://www.tiktok.com/@transfermarkt" onclick="tmEvent('SM-Icons_Header','click','Tiktok');
            " target="_blank">
            <img class="header__icon" height="20" src="https://tmsi.akamaized.net/icons/tiktok.svg" width="20"/>
            </a>
            </div>
            <div class="tm-header__input-wrapper" id="schnellsuche-platz">
            <form action="/schnellsuche/ergebnis/schnellsuche" class="tm-header__form" id="schnellsuche" name="schnellsuche">
            <input autocorrect="off" class="tm-header__input--search-field" name="query" onclick="" placeholder="Enter search term" spellcheck="false" type="text" value="Thomas Muller"/>
            <input alt="search" class="tm-header__input--search-send" type="submit" value=""/>
            </form>
            <a class="tm-header__search-detail" href="/detailsuche/spielerdetail/suche" id="detailsuche-head" title="to the player detail search">
            <img alt="search" class="tm-header__icon-detail-search" height="26" src="https://tmsi.akamaized.net/icons/search_icon_plus_blue_white.svg" width="26"/>
            </a>
            </div>
            </div>
            <nav class="main-navbar navihalter">
            <ul class="main-navbar__container megamenu_dark_bar megamenu_dark" itemscope="itemscope" itemtype="http://www.schema.org/SiteNavigationElement">
            <a class="sticky-logo hide-for-small" href="/">
            <span class="tm_svg" title="Transfermarkt"></span>
            </a>
            <li class="main-navbar__list" data-nav-group="news">
            <span class="main-navbar__list-title tm-main-nav-el" onclick="tmEvent('News','click','menu');
            ">
                        News        </span>
            <div class="main-navbar__drop-down">
            <img class="navigation-loading-spinner" height="40" src="https://tmsi.akamaized.net/icons/tm_spinner_inverted.min.svg" width="40">
            </img></div>
            <li class="main-navbar__list" data-nav-group="transfers">
            <span class="main-navbar__list-title tm-main-nav-el" onclick="tmEvent('Transfers &amp; Gerüchte','click','menu');
            ">
                        Transfers &amp; rumours        </span>
            <div class="main-navbar__drop-down">
            <img class="navigation-loading-spinner" height="40" src="https://tmsi.akamaized.net/icons/tm_spinner_inverted.min.svg" width="40">
            </img></div>
            <li class="main-navbar__list" data-nav-group="marktwerte">
            <span class="main-navbar__list-title tm-main-nav-el" onclick="tmEvent('Marktwerte','click','menu');
            ">
                        Market values        </span>
            <div class="main-navbar__drop-down">
            <img class="navigation-loading-spinner" height="40" src="https://tmsi.akamaized.net/icons/tm_spinner_inverted.min.svg" width="40">
            </img></div>
            <li class="main-navbar__list" data-nav-group="wettbewerbe">
            <span class="main-navbar__list-title tm-main-nav-el" onclick="tmEvent('Wettbewerbe','click','menu');
            ">
                        Competitions        </span>
            <div class="main-navbar__drop-down">
            <img class="navigation-loading-spinner" height="40" src="https://tmsi.akamaized.net/icons/tm_spinner_inverted.min.svg" width="40">
            </img></div>
            <li class="main-navbar__list" data-nav-group="foren">
            <span class="main-navbar__list-title tm-main-nav-el" onclick="tmEvent('Foren','click','menu');
            ">
                        Forums        </span>
            <div class="main-navbar__drop-down">
            <img class="navigation-loading-spinner" height="40" src="https://tmsi.akamaized.net/icons/tm_spinner_inverted.min.svg" width="40">
            </img></div>
            <li class="main-navbar__list" data-nav-group="meintm">
            <span class="main-navbar__list-title tm-main-nav-el" onclick="tmEvent('MeinTM','click','menu');
            ">
                        My TM        </span>
            <div class="main-navbar__drop-down">
            <img class="navigation-loading-spinner" height="40" src="https://tmsi.akamaized.net/icons/tm_spinner_inverted.min.svg" width="40">
            </img></div>
            <li class="main-navbar__list">
            <a class="main-navbar__list-title tm-main-nav-el live-navilink" href="/ticker/index/live" onclick="tmEvent('Live','click','menu');
            ">
                        Live                            <tm-live-match-counter auto-request="true" content='["Live match", "live matches"]'></tm-live-match-counter>
            </a>
            </li>
            </li></li></li></li></li></li></ul>
            <form action="/schnellsuche/ergebnis/schnellsuche" class="noclose sticky-suche" id="schnellsuche-sticky" name="schnellsuche">
            <input class="header-suche" name="query" onclick="" placeholder="Enter search term" type="text"/>
            <input alt="search" class="header-suche-abschicken" src="https://tmssl.akamaized.net//images/suchicon.png" type="image"/>
            </form>
            <a class="header-suche-detailsuche" href="/detailsuche/spielerdetail/suche" id="detailsuche-head" title="to the player detail search">
            <span class="icon-detailsuche"></span>
            </a>
            <a href="#" id="arrow-up-xy">
            <svg enable-background="new 0 0 100 100" height="100px" id="Layer_1" style="fill: white; width: 20px; height: 20px;" version="1.1" viewbox="0 0 100 100" width="100px" x="0px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" y="0px">
            <g>
            <path d="M78.016,49.132L51.961,12.714c-0.471-0.66-1.233-1.049-2.043-1.051c-0.006,0-0.006,0-0.006,0
                                            c-0.815,0.002-1.575,0.396-2.048,1.059L21.977,49.14c-0.546,0.767-0.616,1.776-0.183,2.612c0.426,0.835,1.292,1.361,2.236,1.361
                                            h12.183l-0.001,32.709c0,1.39,1.125,2.515,2.516,2.515l22.541-0.001c1.389,0.001,2.515-1.124,2.516-2.517l0-32.705h12.187
                                            c0.94,0,1.803-0.53,2.237-1.367C78.641,50.911,78.566,49.9,78.016,49.132z"></path>
            </g>
            </svg>
            </a>
            <div class="tm-login" id="login" onclick="tmEvent('login','click','sign_in_button');
            ">
            <svg class="tm-login__image" enable-background="new 0 0 100 100" fill="#FFF" height="100px" id="Layer_1" version="1.1" viewbox="0 0 100 100" width="100px" x="0px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" y="0px">
            <g>
            <path d="M80.161,60.441l-15.66-7.47l-6.622-3.159c2.892-1.822,5.241-4.634,6.778-8.022c1.22-2.69,1.946-5.734,1.946-8.99
                            c0-1.827-0.29-3.562-0.694-5.236C63.94,19.453,57.605,13.477,50,13.477c-7.461,0-13.701,5.763-15.792,13.645
                            c-0.482,1.808-0.815,3.688-0.815,5.68c0,3.459,0.808,6.684,2.181,9.489c1.587,3.254,3.94,5.937,6.804,7.662l-6.342,2.953
                            l-16.168,7.53c-1.404,0.658-2.327,2.242-2.327,4.011v15.062v2.703c0,2.381,1.659,4.312,3.708,4.312h57.505
                            c2.048,0,3.708-1.93,3.708-4.312v-2.703V64.446C82.46,62.683,81.552,61.114,80.161,60.441z"></path>
            </g>
            </svg>
            <span class="tm-login__cta">
                    Log in    </span>
            </div>
            </nav>
            <div class="quick-select-wrapper">
            <div class="ssc" id="quickselect-skeleton" style="height: 40px;">
            <div class="ssc-wrapper flex" style="height: 100%; padding: 0">
            <div class="ssc-square quickselect-element" style="width: 40px;"></div>
            <div class="ssc-square quickselect-element quickselect-selector" style="width: 171.06px;"></div>
            <div class="ssc-square quickselect-element quickselect-selector" style="width: 170.84px;"></div>
            <div class="ssc-square quickselect-element quickselect-selector" style="width: 138.03px;"></div>
            <div class="ssc-square quickselect-element quickselect-selector" style="width: 141.5px;"></div>
            </div>
            </div>
            <tm-quick-select-bar default-club="" default-competition="" default-country="189" default-player="" dropdown-visible="" translations='{"home":"Home","country":"Country","competition":"Competition","club":"club","player":"player","attack":"attack","midfield":"midfield","defense":"defence","goalkeeper":"goalkeeper"}'>
            </tm-quick-select-bar>
            </div>
            <div class="werbung werbung-billboard"><!-- /22272936144,58778164/display_thirdparty/transfermarkt_uk/ros/top_banner -->
            <div id="div-gpt-ad-top_banner" style="min-width: 728px; min-height: 90px;"></div>
            <!-- End AdSlot 2 --></div> </header>
            <main>
            <div class="row">
            <div class="large-12 columns">
            <div class="box">
            <div class="table-header">Search results for players                    - 23 Hits</div>
            <div class="responsive-table">
            <div class="grid-view" id="yw0">
            <div class="summary"></div>
            <table class="items">
            <thead>
            <tr>
            <th id="yw0_c0">Name/Position</th><th class="zentriert" id="yw0_c1">Position</th><th class="zentriert" id="yw0_c2">Club</th><th class="zentriert" id="yw0_c3"><a class="sort-link" href="/schnellsuche/ergebnis/schnellsuche?query=Thomas+Muller&amp;x=0&amp;y=0&amp;sort=age">Age</a></th><th class="zentriert" id="yw0_c4">Nat.</th><th class="rechts" id="yw0_c5"><a class="sort-link" href="/schnellsuche/ergebnis/schnellsuche?query=Thomas+Muller&amp;x=0&amp;y=0&amp;sort=marktwert">Market Value</a></th><th class="rechts" id="yw0_c6">Agents</th></tr>
            </thead>
            <tbody>
            <tr class="odd">
            <td><table class="inline-table"><tr><td rowspan="2"><a href="#"><img alt="Thomas Müller" class="bilderrahmen-fixed" src="https://img.a.transfermarkt.technology/portrait/small/58358-1667830486.jpg?lm=1" title="Thomas Müller"/></a></td><td class="hauptlink"><a href="/thomas-muller/profil/spieler/58358" title="Thomas Müller">Thomas Müller</a></td></tr><tr><td><a href="/fc-bayern-munchen/startseite/verein/27" title="Bayern Munich">Bayern Munich</a></td></tr></table></td><td class="zentriert">SS</td><td class="zentriert"><a href="/fc-bayern-munchen/startseite/verein/27" title="Bayern Munich"><img alt="Bayern Munich" class="tiny_wappen" src="https://tmssl.akamaized.net/images/wappen/tiny/27.png?lm=1498251238" title="Bayern Munich"/></a></td><td class="zentriert">33</td><td class="zentriert"><img alt="Germany" class="flaggenrahmen" src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" title="Germany"/></td><td class="rechts hauptlink">€22.00m</td><td class="rechts"><a href="/kogl-amp-partner-gmbh/beraterfirma/berater/302">Kögl &amp; Partner GmbH</a></td></tr>
            <tr class="even">
            <td><table class="inline-table"><tr><td rowspan="2"><a href="#"><img alt="Thomas Müller" class="bilderrahmen-fixed" src="https://img.a.transfermarkt.technology/portrait/small/default.jpg?lm=1" title="Thomas Müller"/></a></td><td class="hauptlink"><a href="/thomas-muller/profil/spieler/566322" title="Thomas Müller">Thomas Müller</a></td></tr><tr><td>Retired</td></tr></table></td><td class="zentriert">Defender</td><td class="zentriert"><img alt="Retired" class="tiny_wappen" src="https://tmssl.akamaized.net/images/wappen/tiny/123.png?lm=1456997286" title="Retired"/></td><td class="zentriert">52</td><td class="zentriert"><img alt="Switzerland" class="flaggenrahmen" src="https://tmssl.akamaized.net/images/flagge/verysmall/148.png?lm=1520611569" title="Switzerland"/></td><td class="rechts hauptlink">-</td><td class="rechts"></td></tr>
            <tr class="odd">
            <td><table class="inline-table"><tr><td rowspan="2"><a href="#"><img alt="Thomas Müller" class="bilderrahmen-fixed" src="https://img.a.transfermarkt.technology/portrait/small/default.jpg?lm=1" title="Thomas Müller"/></a></td><td class="hauptlink"><a href="/thomas-muller/profil/spieler/607560" title="Thomas Müller">Thomas Müller</a></td></tr><tr><td><a href="/vereinslos/startseite/verein/515" title="Without Club">Without Club</a></td></tr></table></td><td class="zentriert">Attack</td><td class="zentriert"><a href="/vereinslos/startseite/verein/515" title="Without ClubWithout Club"><img alt="Without Club" class="tiny_wappen" src="https://tmssl.akamaized.net/images/wappen/tiny/515.png?lm=1456997255" title="Without Club"/></a></td><td class="zentriert">32</td><td class="zentriert"><img alt="Germany" class="flaggenrahmen" src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" title="Germany"/></td><td class="rechts hauptlink">-</td><td class="rechts"></td></tr>
            <tr class="even">
            <td><table class="inline-table"><tr><td rowspan="2"><a href="#"><img alt="Thomas Müller" class="bilderrahmen-fixed" src="https://img.a.transfermarkt.technology/portrait/small/default.jpg?lm=1" title="Thomas Müller"/></a></td><td class="hauptlink"><a href="/thomas-muller/profil/spieler/624239" title="Thomas Müller">Thomas Müller</a></td></tr><tr><td><a href="/djk-pluwig-gusterath/startseite/verein/58970" title="DJK Pluwig-Gusterath">DJK Pluwig-Gusterath</a></td></tr></table></td><td class="zentriert">midfield</td><td class="zentriert"><a href="/djk-pluwig-gusterath/startseite/verein/58970" title="DJK Pluwig-Gusterath"><img alt="DJK Pluwig-Gusterath" class="tiny_wappen" src="https://tmssl.akamaized.net/images/wappen/tiny/58970.png?lm=1505848382" title="DJK Pluwig-Gusterath"/></a></td><td class="zentriert">25</td><td class="zentriert"><img alt="Germany" class="flaggenrahmen" src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" title="Germany"/></td><td class="rechts hauptlink">-</td><td class="rechts"></td></tr>
            <tr class="odd">
            <td><table class="inline-table"><tr><td rowspan="2"><a href="#"><img alt="Thomas Müller" class="bilderrahmen-fixed" src="https://img.a.transfermarkt.technology/portrait/small/default.jpg?lm=1" title="Thomas Müller"/></a></td><td class="hauptlink"><a href="/thomas-muller/profil/spieler/90887" title="Thomas Müller">Thomas Müller</a></td></tr><tr><td>Retired</td></tr></table></td><td class="zentriert">midfield</td><td class="zentriert"><img alt="Retired" class="tiny_wappen" src="https://tmssl.akamaized.net/images/wappen/tiny/123.png?lm=1456997286" title="Retired"/></td><td class="zentriert">36</td><td class="zentriert"><a href="/intern/faq/#ds_info">N/A</a></td><td class="rechts hauptlink">-</td><td class="rechts"></td></tr>
            <tr class="even">
            <td><table class="inline-table"><tr><td rowspan="2"><a href="#"><img alt="Thomas Müllers" class="bilderrahmen-fixed" src="https://img.a.transfermarkt.technology/portrait/small/default.jpg?lm=1" title="Thomas Müllers"/></a></td><td class="hauptlink"><a href="/thomas-mullers/profil/spieler/712735" title="Thomas Müllers">Thomas Müllers</a></td></tr><tr><td>Retired</td></tr></table></td><td class="zentriert">midfield</td><td class="zentriert"><img alt="Retired" class="tiny_wappen" src="https://tmssl.akamaized.net/images/wappen/tiny/123.png?lm=1456997286" title="Retired"/></td><td class="zentriert">-</td><td class="zentriert"><img alt="Germany" class="flaggenrahmen" src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" title="Germany"/></td><td class="rechts hauptlink">-</td><td class="rechts"></td></tr>
            <tr class="odd">
            <td><table class="inline-table"><tr><td rowspan="2"><a href="#"><img alt="Thomas Müller" class="bilderrahmen-fixed" src="https://img.a.transfermarkt.technology/portrait/small/default.jpg?lm=1" title="Thomas Müller"/></a></td><td class="hauptlink"><a href="/thomas-muller/profil/spieler/130850" title="Thomas Müller">Thomas Müller</a></td></tr><tr><td><a href="/unbekannt/startseite/verein/75" title="Unknown">Unknown</a></td></tr></table></td><td class="zentriert">midfield</td><td class="zentriert"><a href="/unbekannt/startseite/verein/75" title="UnknownUnknown"><img alt="Unknown" class="tiny_wappen" src="https://tmssl.akamaized.net/images/wappen/tiny/75.png?lm=1456997316" title="Unknown"/></a></td><td class="zentriert">35</td><td class="zentriert"><a href="/intern/faq/#ds_info">N/A</a></td><td class="rechts hauptlink">-</td><td class="rechts"></td></tr>
            <tr class="even">
            <td><table class="inline-table"><tr><td rowspan="2"><a href="#"><img alt="Thomas Müller" class="bilderrahmen-fixed" src="https://img.a.transfermarkt.technology/portrait/small/default.jpg?lm=1" title="Thomas Müller"/></a></td><td class="hauptlink"><a href="/thomas-muller/profil/spieler/757364" title="Thomas Müller">Thomas Müller</a></td></tr><tr><td>Retired</td></tr></table></td><td class="zentriert">Attack</td><td class="zentriert"><img alt="Retired" class="tiny_wappen" src="https://tmssl.akamaized.net/images/wappen/tiny/123.png?lm=1456997286" title="Retired"/></td><td class="zentriert">-</td><td class="zentriert"><img alt="Germany" class="flaggenrahmen" src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" title="Germany"/></td><td class="rechts hauptlink">-</td><td class="rechts"></td></tr>
            <tr class="odd">
            <td><table class="inline-table"><tr><td rowspan="2"><a href="#"><img alt="Thomas Müller" class="bilderrahmen-fixed" src="https://img.a.transfermarkt.technology/portrait/small/default.jpg?lm=1" title="Thomas Müller"/></a></td><td class="hauptlink"><a href="/thomas-muller/profil/spieler/145029" title="Thomas Müller">Thomas Müller</a></td></tr><tr><td>Retired</td></tr></table></td><td class="zentriert">GK</td><td class="zentriert"><img alt="Retired" class="tiny_wappen" src="https://tmssl.akamaized.net/images/wappen/tiny/123.png?lm=1456997286" title="Retired"/></td><td class="zentriert">52</td><td class="zentriert"><img alt="Germany" class="flaggenrahmen" src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" title="Germany"/></td><td class="rechts hauptlink">-</td><td class="rechts"></td></tr>
            <tr class="even">
            <td><table class="inline-table"><tr><td rowspan="2"><a href="#"><img alt="Thomas Müller" class="bilderrahmen-fixed" src="https://img.a.transfermarkt.technology/portrait/small/default.jpg?lm=1" title="Thomas Müller"/></a></td><td class="hauptlink"><a href="/thomas-muller/profil/spieler/775953" title="Thomas Müller">Thomas Müller</a></td></tr><tr><td><a href="/sg-ahldorf-muhlen/startseite/verein/67868" title="SG Ahldorf-Mühlen ">SG Ahldorf-Mühlen </a></td></tr></table></td><td class="zentriert">Defender</td><td class="zentriert"><a href="/sg-ahldorf-muhlen/startseite/verein/67868" title="SG Ahldorf-Mühlen "><img alt="SG Ahldorf-Mühlen " class="tiny_wappen" src="https://tmssl.akamaized.net/images/wappen/tiny/67868.png?lm=1532698294" title="SG Ahldorf-Mühlen "/></a></td><td class="zentriert">-</td><td class="zentriert"><img alt="N/A" class="flaggenrahmen" src="https://tmssl.akamaized.net/images/flagge/verysmall/default.png?lm=1520611569" title="N/A"/></td><td class="rechts hauptlink">-</td><td class="rechts"></td></tr>
            </tbody>
            </table>
            <div class="pager"><ul class="tm-pagination">
            <li class="tm-pagination__list-item tm-pagination__list-item--active"><a class="tm-pagination__link" href="/schnellsuche/ergebnis/schnellsuche?query=Thomas+Muller&amp;x=0&amp;y=0" title="Page 1">1</a></li>
            <li class="tm-pagination__list-item"><a class="tm-pagination__link" href="/schnellsuche/ergebnis/schnellsuche?query=Thomas+Muller&amp;x=0&amp;y=0&amp;Spieler_page=2" title="Page 2">2</a></li>
            <li class="tm-pagination__list-item"><a class="tm-pagination__link" href="/schnellsuche/ergebnis/schnellsuche?query=Thomas+Muller&amp;x=0&amp;y=0&amp;Spieler_page=3" title="Page 3">3</a></li>
            <li class="tm-pagination__list-item tm-pagination__list-item--icon-next-page"><a class="tm-pagination__link" href="/schnellsuche/ergebnis/schnellsuche?query=Thomas+Muller&amp;x=0&amp;y=0&amp;Spieler_page=2" title="Go to next page">  </a></li>
            <li class="tm-pagination__list-item tm-pagination__list-item--icon-last-page"><a class="tm-pagination__link" href="/schnellsuche/ergebnis/schnellsuche?query=Thomas+Muller&amp;x=0&amp;y=0&amp;Spieler_page=3" title="Go the last page (page 3)">  </a></li></ul></div><div class="keys" style="display:none" title="/schnellsuche/ergebnis/schnellsuche?query=Thomas%20Muller&amp;x=0&amp;y=0"><span>58358</span><span>566322</span><span>607560</span><span>624239</span><span>90887</span><span>712735</span><span>130850</span><span>757364</span><span>145029</span><span>775953</span></div>
            </div> </div>
            <div class="table-footer">
            <a href="/detailsuche/spielerdetail/suche">
                                                            to the player detail search                    </a>
            </div>
            </div>
            </div>
            </div>
            <div class="row">
            <div class="large-12 columns">
            <div class="box">
            <div class="table-header">Search results: Managers &amp; officials                    - 5 Hits</div>
            <div class="responsive-table">
            <div class="grid-view" id="yw1">
            <div class="summary"></div>
            <table class="items">
            <thead>
            <tr>
            <th id="yw1_c0">Name</th><th class="zentriert" id="yw1_c1">Club</th><th class="zentriert" id="yw1_c2">Age</th><th class="zentriert" id="yw1_c3">Nat.</th><th class="zentriert" id="yw1_c4">Function</th><th class="zentriert" id="yw1_c5">Contract until</th></tr>
            </thead>
            <tbody>
            <tr class="odd">
            <td><table class="inline-table"><tr><td rowspan="2"><a href="#"><img alt="Thomas Müller" class="bilderrahmen-fixed" src="https://img.a.transfermarkt.technology/portrait/small/default.jpg?lm=1" title="Thomas Müller"/></a></td><td class="hauptlink"><a href="/thomas-muller/profil/trainer/21888" id="0" title="Thomas Müller">Thomas Müller</a></td></tr><tr><td><a href="/fc-augsburg/startseite/verein/167" title="FC Augsburg">FC Augsburg</a></td></tr></table></td><td class="zentriert"><a href="/fc-augsburg/startseite/verein/167" title="FC Augsburg"><img alt="FC Augsburg" class="tiny_wappen" src="https://tmssl.akamaized.net/images/wappen/tiny/167.png?lm=1656582897" title="FC Augsburg"/></a></td><td class="zentriert">55</td><td class="zentriert"><img alt="Germany" class="flaggenrahmen" src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" title="Germany"/></td><td class="rechts">Chairman of the Supervisory Board </td><td class="rechts">-</td></tr>
            <tr class="even">
            <td><table class="inline-table"><tr><td rowspan="2"><a href="#"><img alt="Thomas Müller" class="bilderrahmen-fixed" src="https://img.a.transfermarkt.technology/portrait/small/default.jpg?lm=1" title="Thomas Müller"/></a></td><td class="hauptlink"><a href="/thomas-muller/profil/trainer/24969" id="0" title="Thomas Müller">Thomas Müller</a></td></tr><tr><td><a href="/vereinslos/startseite/verein/515" title="Without Club">Without Club</a></td></tr></table></td><td class="zentriert"><a href="/vereinslos/startseite/verein/515" title="Without ClubWithout Club"><img alt="Without Club" class="tiny_wappen" src="https://tmssl.akamaized.net/images/wappen/tiny/515.png?lm=1456997255" title="Without Club"/></a></td><td class="zentriert">-</td><td class="zentriert"><img alt="Germany" class="flaggenrahmen" src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" title="Germany"/></td><td class="rechts">Goalkeeping Coach</td><td class="rechts">-</td></tr>
            <tr class="odd">
            <td><table class="inline-table"><tr><td rowspan="2"><a href="#"><img alt="Thomas Müller" class="bilderrahmen-fixed" src="https://img.a.transfermarkt.technology/portrait/small/default.jpg?lm=1" title="Thomas Müller"/></a></td><td class="hauptlink"><a href="/thomas-muller/profil/trainer/54646" id="0" title="Thomas Müller">Thomas Müller</a></td></tr><tr><td><a href="/heidmuhler-fc/startseite/verein/7766" title="Heidmühler FC">Heidmühler FC</a></td></tr></table></td><td class="zentriert"><a href="/heidmuhler-fc/startseite/verein/7766" title="Heidmühler FC"><img alt="Heidmühler FC" class="tiny_wappen" src="https://tmssl.akamaized.net/images/wappen/tiny/7766.png?lm=1520610104" title="Heidmühler FC"/></a></td><td class="zentriert">-</td><td class="zentriert"><img alt="Germany" class="flaggenrahmen" src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" title="Germany"/></td><td class="rechts">Goalkeeping Coach</td><td class="rechts">-</td></tr>
            <tr class="even">
            <td><table class="inline-table"><tr><td rowspan="2"><a href="#"><img alt="Thomas Müllers" class="bilderrahmen-fixed" src="https://img.a.transfermarkt.technology/portrait/small/default.jpg?lm=1" title="Thomas Müllers"/></a></td><td class="hauptlink"><a href="/thomas-mullers/profil/trainer/73366" id="0" title="Thomas Müllers">Thomas Müllers</a></td></tr><tr><td><a href="/tsv-kaldenkirchen-u19/startseite/verein/76978" title="TSV Kaldenkirchen U19">TSV Kaldenkirchen U19</a></td></tr></table></td><td class="zentriert"><a href="/tsv-kaldenkirchen-u19/startseite/verein/76978" title="TSV Kaldenkirchen U19"><img alt="TSV Kaldenkirchen U19" class="tiny_wappen" src="https://tmssl.akamaized.net/images/wappen/tiny/76978.png?lm=1573295700" title="TSV Kaldenkirchen U19"/></a></td><td class="zentriert">-</td><td class="zentriert"><img alt="Germany" class="flaggenrahmen" src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" title="Germany"/></td><td class="rechts">Manager</td><td class="rechts">-</td></tr>
            <tr class="odd">
            <td><table class="inline-table"><tr><td rowspan="2"><a href="#"><img alt="Thomas Müller" class="bilderrahmen-fixed" src="https://img.a.transfermarkt.technology/portrait/small/default.jpg?lm=1" title="Thomas Müller"/></a></td><td class="hauptlink"><a href="/thomas-muller/profil/trainer/85186" id="0" title="Thomas Müller">Thomas Müller</a></td></tr><tr><td><a href="/tsv-roddenau/startseite/verein/29799" title="TSV Röddenau">TSV Röddenau</a></td></tr></table></td><td class="zentriert"><a href="/tsv-roddenau/startseite/verein/29799" title="TSV Röddenau"><img alt="TSV Röddenau" class="tiny_wappen" src="https://tmssl.akamaized.net/images/wappen/tiny/29799.png?lm=1480872128" title="TSV Röddenau"/></a></td><td class="zentriert">-</td><td class="zentriert"><img alt="Germany" class="flaggenrahmen" src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" title="Germany"/></td><td class="rechts">Head of Football Operations</td><td class="rechts">-</td></tr>
            </tbody>
            </table>
            <div class="keys" style="display:none" title="/schnellsuche/ergebnis/schnellsuche?query=Thomas%20Muller&amp;x=0&amp;y=0"><span>21888</span><span>24969</span><span>54646</span><span>73366</span><span>85186</span></div>
            </div> </div>
            </div>
            </div>
            </div>
            <div class="box"><script async="" src="https://fcp.codes/embed-code-template/embed-code-template.js#SMART_91f60932-b199-4dbc-8630-16ac5e06b884"></script>
            </div> <div class="row">
            <div class="large-12 columns">
            <div class="box">
            <div class="table-header">Search results for agents                    - 22 Hits</div>
            <div class="responsive-table">
            <div class="grid-view" id="yw3">
            <div class="summary"></div>
            <table class="items">
            <thead>
            <tr>
            <th class="zentriert" id="yw3_c0">Premium Service</th><th class="zentriert" id="yw3_c1">Company</th><th class="zentriert" id="yw3_c2">Licence</th><th id="yw3_c3">Agents</th></tr>
            </thead>
            <tbody>
            <tr class="odd">
            <td class="zentriert"><span class="icon-berater-adresseintrag icons_sprite" title="active"> </span></td><td class="zentriert"><table class="inline-table" gmbh="" title="Soccertalk">
            <tr>
            <td rowspan="2">
            <a href="/berater/beraterfirma?id=65"><img alt="-" class="berater-logorahmen" src="https://tmssl.akamaized.net/images/berater_logo/small/berater-default.png?lm=1520606995" title="Soccertalk GmbH"/></a>
            </td>
            <td class="hauptlink"><a href="/soccertalk-gmbh/beraterfirma/berater/65">Soccertalk GmbH</a></td></tr>
            </table></td><td class="zentriert"><img src="https://tmsi.akamaized.net/icons/playeragent_license_agent_small.png" title="Player agent"/></td><td>Alen Augustincic</td></tr>
            <tr class="even">
            <td class="zentriert"><span class="icon-berater-adresseintrag icons_sprite" title="active"> </span></td><td class="zentriert"><table agency="" class="inline-table" fairplay="" ltd="" title="FPA">
            <tr>
            <td rowspan="2">
            <a href="/berater/beraterfirma?id=770"><img alt="-" class="berater-logorahmen" src="https://tmssl.akamaized.net/images/berater_logo/small/berater-default.png?lm=1520606995" title="FPA Fairplay Agency Ltd"/></a>
            </td>
            <td class="hauptlink"><a href="/fpa-fairplay-agency-ltd/beraterfirma/berater/770">FPA Fairplay Agency Ltd</a></td></tr>
            </table></td><td class="zentriert"><img src="https://tmsi.akamaized.net/icons/playeragent_license_agent_small.png" title="Player agent"/></td><td>Dino Lamberti</td></tr>
            <tr class="odd">
            <td class="zentriert"><span class="icon-berater-adresseintrag icons_sprite" title="active"> </span></td><td class="zentriert"><table &="" class="inline-table" co.="" du="" eventmanagement="" gmbh="" kg="" sport-="" title="Intersoccer" und="">
            <tr>
            <td rowspan="2">
            <a href="/berater/beraterfirma?id=5284"><img alt="-" class="berater-logorahmen" src="https://tmssl.akamaized.net/images/berater_logo/small/berater-default.png?lm=1520606995" title="Intersoccer DU Sport- und Eventmanagement GmbH &amp; Co. KG"/></a>
            </td>
            <td class="hauptlink"><a href="/intersoccer-du-sport-und-eventmanagement-gmbh-amp-co-kg/beraterfirma/berater/5284">Intersoccer DU Sport- und Eventmanagement GmbH &amp; Co. KG</a></td></tr>
            </table></td><td class="zentriert"><img src="https://tmsi.akamaized.net/icons/playeragent_license_agent_small.png" title="Player agent"/></td><td>Werner Franzen</td></tr>
            <tr class="even">
            <td class="zentriert"><span class="icon-berater-adresseintrag icons_sprite" title="active"> </span></td><td class="zentriert"><table class="inline-table" sports="" title="Baha11">
            <tr>
            <td rowspan="2">
            <a href="/berater/beraterfirma?id=2220"><img alt="-" class="berater-logorahmen" src="https://tmssl.akamaized.net/images/berater_logo/small/berater-default.png?lm=1520606995" title="Baha11 Sports"/></a>
            </td>
            <td class="hauptlink"><a href="/baha11-sports/beraterfirma/berater/2220">Baha11 Sports</a></td></tr>
            </table></td><td class="zentriert"> </td><td>Heiko Müller</td></tr>
            <tr class="odd">
            <td class="zentriert"><span class="icon-berater-keinadresseintrag icons_sprite" title="inactive"> </span></td><td class="zentriert"><table class="inline-table" deutsche="" fussball="" gmbh="" invest="" title="DFI">
            <tr>
            <td rowspan="2">
            <a href="/berater/beraterfirma?id=2476"><img alt="-" class="berater-logorahmen" src="https://tmssl.akamaized.net/images/berater_logo/small/berater-default.png?lm=1520606995" title="DFI Deutsche Fussball Invest GmbH"/></a>
            </td>
            <td class="hauptlink"><a href="/dfi-deutsche-fussball-invest-gmbh/beraterfirma/berater/2476">DFI Deutsche Fussball Invest GmbH</a></td></tr>
            </table></td><td class="zentriert"><img src="https://tmsi.akamaized.net/icons/playeragent_license_agent_small.png" title="Player agent"/></td><td>Marco Kowalewski</td></tr>
            <tr class="even">
            <td class="zentriert"><span class="icon-berater-keinadresseintrag icons_sprite" title="inactive"> </span></td><td class="zentriert"><table class="inline-table" digital="" management="" sport="" title="Muller">
            <tr>
            <td rowspan="2">
            <a href="/berater/beraterfirma?id=6538"><img alt="-" class="berater-logorahmen" src="https://tmssl.akamaized.net/images/berater_logo/small/berater-default.png?lm=1520606995" title="Muller Digital Sport Management"/></a>
            </td>
            <td class="hauptlink"><a href="/muller-digital-sport-management/beraterfirma/berater/6538">Muller Digital Sport Management</a></td></tr>
            </table></td><td class="zentriert"><img src="https://tmsi.akamaized.net/icons/playeragent_license_agent_small.png" title="Player agent"/></td><td>Mulugeta Woldemichael</td></tr>
            <tr class="odd">
            <td class="zentriert"><span class="icon-berater-keinadresseintrag icons_sprite" title="inactive"> </span></td><td class="zentriert"><table agency="" class="inline-table" sports="" title="MÜLLER">
            <tr>
            <td rowspan="2">
            <a href="/berater/beraterfirma?id=5389"><img alt="-" class="berater-logorahmen" src="https://tmssl.akamaized.net/images/berater_logo/small/berater-default.png?lm=1520606995" title="MÜLLER SPORTS AGENCY"/></a>
            </td>
            <td class="hauptlink"><a href="/muller-sports-agency/beraterfirma/berater/5389">MÜLLER SPORTS AGENCY</a></td></tr>
            </table></td><td class="zentriert"><img src="https://tmsi.akamaized.net/icons/playeragent_license_agent_small.png" title="Player agent"/></td><td>Oliver Mueller</td></tr>
            <tr class="even">
            <td class="zentriert"><span class="icon-berater-keinadresseintrag icons_sprite" title="inactive"> </span></td><td class="zentriert"><table class="inline-table" football="" title="AGN">
            <tr>
            <td rowspan="2">
            <a href="/berater/beraterfirma?id=2872"><img alt="-" class="berater-logorahmen" src="https://tmssl.akamaized.net/images/berater_logo/small/berater-default.png?lm=1520606995" title="AGN Football"/></a>
            </td>
            <td class="hauptlink"><a href="/agn-football/beraterfirma/berater/2872">AGN Football</a></td></tr>
            </table></td><td class="zentriert"><img src="https://tmsi.akamaized.net/icons/playeragent_license_agent_small.png" title="Player agent"/></td><td>Matheus Assaf</td></tr>
            <tr class="odd">
            <td class="zentriert"><span class="icon-berater-keinadresseintrag icons_sprite" title="inactive"> </span></td><td class="zentriert"><table class="inline-table" fußball-management="" title="MüKa">
            <tr>
            <td rowspan="2">
            <a href="/berater/beraterfirma?id=1509"><img alt="-" class="berater-logorahmen" src="https://tmssl.akamaized.net/images/berater_logo/small/berater-default.png?lm=1520606995" title="MüKa Fußball-Management"/></a>
            </td>
            <td class="hauptlink"><a href="/muka-fussball-management/beraterfirma/berater/1509">MüKa Fußball-Management</a></td></tr>
            </table></td><td class="zentriert"><img src="https://tmsi.akamaized.net/icons/playeragent_license_lawyer_small.png" title="Attorney"/></td><td>Rolf Müller</td></tr>
            <tr class="even">
            <td class="zentriert"><span class="icon-berater-keinadresseintrag icons_sprite" title="inactive"> </span></td><td class="zentriert"><table class="inline-table" gmbh="" sport="" title="PAW">
            <tr>
            <td rowspan="2">
            <a href="/berater/beraterfirma?id=1712"><img alt="-" class="berater-logorahmen" src="https://tmssl.akamaized.net/images/berater_logo/small/berater-default.png?lm=1520606995" title="PAW Sport GmbH"/></a>
            </td>
            <td class="hauptlink"><a href="/paw-sport-gmbh/beraterfirma/berater/1712">PAW Sport GmbH</a></td></tr>
            </table></td><td class="zentriert"><img src="https://tmsi.akamaized.net/icons/playeragent_license_lawyer_small.png" title="Attorney"/></td><td>Michael Müller</td></tr>
            </tbody>
            </table>
            <div class="pager"><ul class="tm-pagination">
            <li class="tm-pagination__list-item tm-pagination__list-item--active"><a class="tm-pagination__link" href="/schnellsuche/ergebnis/schnellsuche?query=Thomas+Muller&amp;x=0&amp;y=0" title="Page 1">1</a></li>
            <li class="tm-pagination__list-item"><a class="tm-pagination__link" href="/schnellsuche/ergebnis/schnellsuche?query=Thomas+Muller&amp;x=0&amp;y=0&amp;page=2" title="Page 2">2</a></li>
            <li class="tm-pagination__list-item"><a class="tm-pagination__link" href="/schnellsuche/ergebnis/schnellsuche?query=Thomas+Muller&amp;x=0&amp;y=0&amp;page=3" title="Page 3">3</a></li>
            <li class="tm-pagination__list-item tm-pagination__list-item--icon-next-page"><a class="tm-pagination__link" href="/schnellsuche/ergebnis/schnellsuche?query=Thomas+Muller&amp;x=0&amp;y=0&amp;page=2" title="Go to next page">  </a></li>
            <li class="tm-pagination__list-item tm-pagination__list-item--icon-last-page"><a class="tm-pagination__link" href="/schnellsuche/ergebnis/schnellsuche?query=Thomas+Muller&amp;x=0&amp;y=0&amp;page=3" title="Go the last page (page 3)">  </a></li></ul></div><div class="keys" style="display:none" title="/schnellsuche/ergebnis/schnellsuche?query=Thomas%20Muller&amp;x=0&amp;y=0"><span>65</span><span>770</span><span>5284</span><span>2220</span><span>2476</span><span>6538</span><span>5389</span><span>2872</span><span>1509</span><span>1712</span></div>
            </div> </div>
            </div>
            </div>
            </div>
            <div class="row">
            <div class="large-12 columns">
            <div class="box">
            <div class="table-header">Search results for referees                    - 2 Hits</div>
            <div class="responsive-table">
            <div class="grid-view" id="yw4">
            <div class="summary"></div>
            <table class="items">
            <thead>
            <tr>
            <th id="yw4_c0">Name/Club</th><th id="yw4_c1"><a class="sort-link" href="/schnellsuche/ergebnis/schnellsuche?query=Thomas+Muller&amp;x=0&amp;y=0&amp;Schiedsrichter_sort=wohnort">Residence</a></th><th class="zentriert" id="yw4_c2">Age</th><th class="zentriert" id="yw4_c3">Nat.</th><th id="yw4_c4">FIFA referee</th></tr>
            </thead>
            <tbody>
            <tr class="odd">
            <td><table class="inline-table"><tr><td rowspan="2"><a href="#"><img alt="Thomas Müller" class="bilderrahmen-fixed" src="https://img.a.transfermarkt.technology/portrait/small/default.jpg?lm=1" title="Thomas Müller"/></a></td><td class="hauptlink"><a href="/thomas-muller/profil/schiedsrichter/10406" title="Thomas Müller">Thomas Müller</a></td></tr></table></td><td></td><td class="zentriert">-</td><td class="zentriert"><img alt="Germany" class="flaggenrahmen" src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" title="Germany"/></td><td></td></tr>
            <tr class="even">
            <td><table class="inline-table"><tr><td rowspan="2"><a href="#"><img alt="Magnus-Thomas Müller" class="bilderrahmen-fixed" src="https://img.a.transfermarkt.technology/portrait/small/default.jpg?lm=1" title="Magnus-Thomas Müller"/></a></td><td class="hauptlink"><a href="/magnus-thomas-muller/profil/schiedsrichter/14456" title="Magnus-Thomas Müller">Magnus-Thomas Müller</a></td></tr></table></td><td>Weißenfels</td><td class="zentriert">26</td><td class="zentriert"><img alt="Germany" class="flaggenrahmen" src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" title="Germany"/></td><td></td></tr>
            </tbody>
            </table>
            <div class="keys" style="display:none" title="/schnellsuche/ergebnis/schnellsuche?query=Thomas%20Muller&amp;x=0&amp;y=0"><span>10406</span><span>14456</span></div>
            </div> </div>
            </div>
            </div>
            </div>
            <style>
                    <!--
                    .icon-transfer-grey {
                        background-position: -375px -26px;
                        width: 15px;
                        height: 15px;
                        vertical-align: middle;
                        cursor: pointer !important;
                    }

                    .icon-stadion-grey {
                        background-position: -656px -30px;
                        width: 29px;
                        height: 15px;
                        vertical-align: middle;
                        cursor: pointer !important;
                    }

                    -->
                </style>
            <div class="werbung werbung-fullsize_contentad"><!-- /22272936144,58778164/display_thirdparty/transfermarkt_uk/ros/bottom_banner -->
            <div id="div-gpt-ad-bottom_banner" style="min-width: 728px; min-height: 90px;"></div>
            <!-- End AdSlot 7 --></div> </main>
            <footer>
            <tm-language-hint></tm-language-hint>
            <div class="tm-footer">
            <a class="tm-footer__logo" href="/">
            <img alt="Transfermarkt" height="33" src="https://tmsi.akamaized.net/head/transfermarkt_logo.svg" width="80"/>
            </a>
            <ul class="tm-footer__links">
            <li class="tm-footer__links-item">
            <a href="/intern/impressum">
                    Legal notice      </a>
            </li>
            <li class="tm-footer__links-item">
            <a href="/intern/web/datenschutz">
                    Data protection      </a>
            </li>
            <li class="tm-footer__links-item">
            <a class="cmp-link" href="javascript:void(0)">
                    Privacy      </a>
            </li>
            <li class="tm-footer__links-item">
            <a href="/intern/anb">
                    General terms of use      </a>
            </li>
            <li class="tm-footer__links-item">
            <a href="/intern/tmteam">
                    The TM team      </a>
            </li>
            <li class="tm-footer__links-item">
            <a href="/intern/faq">
                    FAQ      </a>
            </li>
            <li class="tm-footer__links-item">
            <a href="/intern/fehlermelden">
                    Found a mistake?      </a>
            </li>
            </ul>
            </div>
            </footer>
            <div id="menue_overlay"></div>
            </div>
            <script type="text/javascript">
                            var iam_data = {
            "st":"transfer",
            "cp":"ausland_co.uk_r",
            "co":""
            }
                        </script>
            <script type="module">
                            var defaultOptions={tracking:!0,refreshAds:!0};export var refreshAd=function(){var e,n;[ASCDP.hasOwnProperty("adS"),null===(e=ASCDP.adS)||void 0===e?void 0:e.hasOwnProperty("reloadAds"),"function"==typeof(null===(n=ASCDP.adS)||void 0===n?void 0:n.reloadAds)].every(function(e){return e})&&ASCDP.adS.reloadAds()};export var TmTrackingAndAds=function(e,n){void 0===n&&(n=defaultOptions);var r=["tabelle","reiter","forum"].includes(e)?e:"";n.tracking&&(gtag("event","page_view",{page_path:"/jsContent"+window.location.pathname}),sendIvwData(r)),n.refreshAds&&"undefined"!=typeof ASCDP&&refreshAd()};window.tmTrackingAndAds=function(e,n){return TmTrackingAndAds(e,n)};
                        </script>
            <script type="text/javascript">
                            if(typeof IOMm === 'function') {
                                IOMm('configure', { st: iam_data.st, dn: 'data-84a0f3455d.transfermarkt.co.uk', mh:5 });
                                IOMm('pageview', { cp: iam_data.cp, co: iam_data.co });
                            } else {
                                console.warn('IOMm is not defined');
                            }
                        </script>
            <script type="text/javascript">
                    if(typeof(adet) == "boolean" && adet == false){
                            img_src="/static/singlepictures/jk99hhfsdh209nbnkjldgh90sghfsdlk";
                    } else {
                            img_src="/static/singlepictures/jku90whjlkjbwbta1g4b8h89fh8sgh8d";
                    }
                    var elem = document.createElement("img");
                    document.body.appendChild(elem);
                    elem.src = img_src;
            </script>
            <script>
                                $(function() {
                                    var cnt = $('div.large-4.columns').length;
                                    if (cnt == 1) {
                                        var sidebarDiv = document.querySelector('div.large-4.columns');
                                        if (sidebarDiv !== null) {
                                            $('#werbung_recommender_sidebar_wrapper').appendTo(sidebarDiv);
                                            $('#werbung_recommender_sidebar_wrapper').show();
                                        }
                                    }
                                });
                            </script>
            <div id="werbung_recommender_sidebar_wrapper" style="display: none;">
            <div class="box" id="recommender_sidebar">
            <div class="OUTBRAIN" data-ob-template="DE_Transfermarkt.uk" data-src="https://www.transfermarkt.co.uk/schnellsuche/ergebnis/schnellsuche?query=Thomas%20Muller&amp;x=0&amp;y=0" data-widget-id="SB_1"></div>
            <script async="async" src="//widgets.outbrain.com/outbrain.js" type="text/javascript"></script>
            </div>
            </div>
            <script defer="" src="https://tmsi.akamaized.net/js/globals/tm-global-elements.esm.js" type="module"></script><script defer="" nomodule="" src="https://tmsi.akamaized.net/js/globals/tm-global-elements.js"></script> <script src="https://tmssl.akamaized.net/assets/aa69c6e9c51f1e811847082c63633956/gridview/jquery.yiigridview.js?lm=1667566935" type="text/javascript"></script>
            <script src="https://tmssl.akamaized.net/js/custom/tm-menu.min.js?lm=1667566934" type="text/javascript"></script>
            <script src="https://tmssl.akamaized.net/js/custom/vendors.min.js?lm=1667566934" type="text/javascript"></script>
            <script type="text/javascript">
            /*<![CDATA[*/
                    var loginUrl='/profil/login';
                    var onlyDE = '';
                    var onlyMobile = '';
                    var onlyTablet = '';
                    var getUserID = '';

            function sendIvwData(typ) {
                if(typ == 'tabelle') {
                    var iam_data = {
            "st":"transfer",
            "cp":"ausland_co.uk_r_t",
            "co":""
            }

                }else if(typ == 'reiter') {
                    var iam_data = {
            "st":"transfer",
            "cp":"ausland_co.uk_r_r",
            "co":""
            }

                }else if(typ == 'forum') {
                    var iam_data = {
            "st":"transfer",
            "cp":"ausland_co.uk_r_forum",
            "co":""
            }

                }else {
                    var iam_data = {
            "st":"transfer",
            "cp":"ausland_co.uk_r_s",
            "co":""
            }

                }
                if(typeof IOMm === 'function') {
                    IOMm('pageview', { cp: iam_data.cp, co: iam_data.co });
                }
            }
            jQuery(function($) {
            jQuery('#yw0').yiiGridView({'ajaxUpdate':['yw0'],'ajaxVar':'ajax','pagerClass':'pager','loadingClass':'grid\x2Dview\x2Dloading','filterClass':'filters','tableClass':'items','selectableRows':1,'enableHistory':false,'updateSelector':'\x7Bpage\x7D,\x20\x7Bsort\x7D','filterSelector':'\x7Bfilter\x7D','pageVar':'Spieler_page'});
            jQuery('#yw1').yiiGridView({'ajaxUpdate':['yw1'],'ajaxVar':'ajax','pagerClass':'pager','loadingClass':'grid\x2Dview\x2Dloading','filterClass':'filters','tableClass':'items','selectableRows':1,'enableHistory':false,'updateSelector':'\x7Bpage\x7D,\x20\x7Bsort\x7D','filterSelector':'\x7Bfilter\x7D','pageVar':'Trainer_page'});
            jQuery('#yw3').yiiGridView({'ajaxUpdate':['yw3'],'ajaxVar':'ajax','pagerClass':'pager','loadingClass':'grid\x2Dview\x2Dloading','filterClass':'filters','tableClass':'items','selectableRows':1,'enableHistory':false,'updateSelector':'\x7Bpage\x7D,\x20\x7Bsort\x7D','filterSelector':'\x7Bfilter\x7D','pageVar':'page'});
            jQuery('#yw4').yiiGridView({'ajaxUpdate':['yw4'],'ajaxVar':'ajax','pagerClass':'pager','loadingClass':'grid\x2Dview\x2Dloading','filterClass':'filters','tableClass':'items','selectableRows':1,'enableHistory':false,'updateSelector':'\x7Bpage\x7D,\x20\x7Bsort\x7D','filterSelector':'\x7Bfilter\x7D','pageVar':'Schiedsrichter_page'});
            });
            /*]]>*/
            </script>
            </body>
            </html>
        """
    soup = BeautifulSoup(html_code, "html.parser")
    return soup


@pytest.fixture
def detailed_view_soup():
    html_code = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
            <script type="text/javascript">
                !function () { var e = function () { var e, t = "__tcfapiLocator", a = [], n = window; for (; n;) { try { if (n.frames[t]) { e = n; break } } catch (e) { } if (n === window.top) break; n = n.parent } e || (!function e() { var a = n.document, r = !!n.frames[t]; if (!r) if (a.body) { var i = a.createElement("iframe"); i.style.cssText = "display:none", i.name = t, a.body.appendChild(i) } else setTimeout(e, 5); return !r }(), n.__tcfapi = function () { for (var e, t = arguments.length, n = new Array(t), r = 0; r < t; r++)n[r] = arguments[r]; if (!n.length) return a; if ("setGdprApplies" === n[0]) n.length > 3 && 2 === parseInt(n[1], 10) && "boolean" == typeof n[3] && (e = n[3], "function" == typeof n[2] && n[2]("set", !0)); else if ("ping" === n[0]) { var i = { gdprApplies: e, cmpLoaded: !1, cmpStatus: "stub" }; "function" == typeof n[2] && n[2](i) } else a.push(n) }, n.addEventListener("message", (function (e) { var t = "string" == typeof e.data, a = {}; try { a = t ? JSON.parse(e.data) : e.data } catch (e) { } var n = a.__tcfapiCall; n && window.__tcfapi(n.command, n.version, (function (a, r) { var i = { __tcfapiReturn: { returnValue: a, success: r, callId: n.callId } }; t && (i = JSON.stringify(i)), e.source.postMessage(i, "*") }), n.parameter) }), !1)) }; "undefined" != typeof module ? module.exports = e : e() }();
            </script>
            <script>
            window._sp_ = {
                config: {"accountId":1254,"propertyId":7426,"gdpr":{"consentLanguage":"en"},"baseEndpoint":"https://cdn.privacy-mgmt.com"}}
            </script>
            <meta charset="utf-8"/>
            <div class="werbung werbung-header"><!-- Start GPT Tag -->
            <script src="https://lngtd.com/transfermarkt_ros.js"></script>
            <!-- End GPT Tag --></div> </link></link></head>
            <body class="" data-cmp-layer-id="225254" data-tm-tld="uk" itemscope="" itemtype="http://schema.org/WebPage">
            <div id="main">
            <div class="werbung-skyscraper-container">
            <div class="werbung werbung-skyscraper"><!-- /22272936144,58778164/display_thirdparty/transfermarkt_uk/ros/skyscraper -->
            <div id="div-gpt-ad-skyscrape" style="min-width: 160px; min-height: 600px;"></div>
            <!-- End AdSlot 1 --></div> </div>
            <div class="werbung-skyscraperbtf-container">
            </div>
            <header class="tm-header">
            <div class="tm-header__box">
            <a href="/">
            <img alt="Transfermarkt" class="icon-logo" height="62" src="https://tmsi.akamaized.net/head/transfermarkt_logo.svg" title="Transfermarkt" width="156"/>
            </a>
            <tm-domainswitcher open-list="false" tld="co.uk"></tm-domainswitcher>
            <div class="tm-header__social-box">
            <a class="header__social-link" href="https://www.facebook.com/transfermarkt.co.uk" onclick="tmEvent('SM-Icons_Header','click','Facebook');
            " target="_blank">
            <img class="header__icon" height="20" src="https://tmsi.akamaized.net/icons/socialMedia/fb_icon_hover.svg" width="20"/>
            </a>
            <a class="header__social-link" href="http://twitter.com/TMuk_news" onclick="tmEvent('SM-Icons_Header','click','Twitter');
            " target="_blank">
            <img class="header__icon" height="20" src="https://tmsi.akamaized.net/icons/socialMedia/twitter_icon_hover.svg" width="20"/>
            </a>
            <a class="header__social-link" href="http://instagram.com/transfermarkt_official" onclick="tmEvent('SM-Icons_Header','click','Instagram');
            " target="_blank">
            <img class="header__icon" height="20" src="https://tmsi.akamaized.net/icons/socialMedia/instagram_icon_hover.svg" width="20"/>
            </a>
            <a class="header__social-link" href="/intern/rssguide" onclick="tmEvent('SM-Icons_Header','click','RSS');
            " target="_blank">
            <img class="header__icon" height="20" src="https://tmsi.akamaized.net/icons/socialMedia/rss_icon_hover.svg" width="20"/>
            </a>
            <a class="header__social-link" href="https://www.tiktok.com/@transfermarkt" onclick="tmEvent('SM-Icons_Header','click','Tiktok');
            " target="_blank">
            <img class="header__icon" height="20" src="https://tmsi.akamaized.net/icons/tiktok.svg" width="20"/>
            </a>
            </div>
            <div class="tm-header__input-wrapper" id="schnellsuche-platz">
            <form action="/schnellsuche/ergebnis/schnellsuche" class="tm-header__form" id="schnellsuche" name="schnellsuche">
            <input autocorrect="off" class="tm-header__input--search-field" name="query" onclick="" placeholder="Enter search term" spellcheck="false" type="text" value=""/>
            <input alt="search" class="tm-header__input--search-send" type="submit" value=""/>
            </form>
            <a class="tm-header__search-detail" href="/detailsuche/spielerdetail/suche" id="detailsuche-head" title="to the player detail search">
            <img alt="search" class="tm-header__icon-detail-search" height="26" src="https://tmsi.akamaized.net/icons/search_icon_plus_blue_white.svg" width="26"/>
            </a>
            </div>
            </div>
            <nav class="main-navbar navihalter">
            <ul class="main-navbar__container megamenu_dark_bar megamenu_dark" itemscope="itemscope" itemtype="http://www.schema.org/SiteNavigationElement">
            <a class="sticky-logo hide-for-small" href="/">
            <span class="tm_svg" title="Transfermarkt"></span>
            </a>
            <li class="main-navbar__list" data-nav-group="news">
            <span class="main-navbar__list-title tm-main-nav-el" onclick="tmEvent('News','click','menu');
            ">
                        News        </span>
            <div class="main-navbar__drop-down">
            <img class="navigation-loading-spinner" height="40" src="https://tmsi.akamaized.net/icons/tm_spinner_inverted.min.svg" width="40">
            </img></div>
            <li class="main-navbar__list" data-nav-group="transfers">
            <span class="main-navbar__list-title tm-main-nav-el" onclick="tmEvent('Transfers &amp; Gerüchte','click','menu');
            ">
                        Transfers &amp; rumours        </span>
            <div class="main-navbar__drop-down">
            <img class="navigation-loading-spinner" height="40" src="https://tmsi.akamaized.net/icons/tm_spinner_inverted.min.svg" width="40">
            </img></div>
            <li class="main-navbar__list" data-nav-group="marktwerte">
            <span class="main-navbar__list-title tm-main-nav-el" onclick="tmEvent('Marktwerte','click','menu');
            ">
                        Market values        </span>
            <div class="main-navbar__drop-down">
            <img class="navigation-loading-spinner" height="40" src="https://tmsi.akamaized.net/icons/tm_spinner_inverted.min.svg" width="40">
            </img></div>
            <li class="main-navbar__list aktiv" data-nav-group="wettbewerbe">
            <span class="main-navbar__list-title tm-main-nav-el" onclick="tmEvent('Wettbewerbe','click','menu');
            ">
                        Competitions        </span>
            <div class="main-navbar__drop-down">
            <img class="navigation-loading-spinner" height="40" src="https://tmsi.akamaized.net/icons/tm_spinner_inverted.min.svg" width="40">
            </img></div>
            <li class="main-navbar__list" data-nav-group="foren">
            <span class="main-navbar__list-title tm-main-nav-el" onclick="tmEvent('Foren','click','menu');
            ">
                        Forums        </span>
            <div class="main-navbar__drop-down">
            <img class="navigation-loading-spinner" height="40" src="https://tmsi.akamaized.net/icons/tm_spinner_inverted.min.svg" width="40">
            </img></div>
            <li class="main-navbar__list" data-nav-group="meintm">
            <span class="main-navbar__list-title tm-main-nav-el" onclick="tmEvent('MeinTM','click','menu');
            ">
                        My TM        </span>
            <div class="main-navbar__drop-down">
            <img class="navigation-loading-spinner" height="40" src="https://tmsi.akamaized.net/icons/tm_spinner_inverted.min.svg" width="40">
            </img></div>
            <li class="main-navbar__list">
            <a class="main-navbar__list-title tm-main-nav-el live-navilink" href="/ticker/index/live" onclick="tmEvent('Live','click','menu');
            ">
                        Live                            <tm-live-match-counter auto-request="true" content='["Live match", "live matches"]'></tm-live-match-counter>
            </a>
            </li>
            </li></li></li></li></li></li></ul>
            <form action="/schnellsuche/ergebnis/schnellsuche" class="noclose sticky-suche" id="schnellsuche-sticky" name="schnellsuche">
            <input class="header-suche" name="query" onclick="" placeholder="Enter search term" type="text"/>
            <input alt="search" class="header-suche-abschicken" src="https://tmssl.akamaized.net//images/suchicon.png" type="image"/>
            </form>
            <a class="header-suche-detailsuche" href="/detailsuche/spielerdetail/suche" id="detailsuche-head" title="to the player detail search">
            <span class="icon-detailsuche"></span>
            </a>
            <a href="#" id="arrow-up-xy">
            <svg enable-background="new 0 0 100 100" height="100px" id="Layer_1" style="fill: white; width: 20px; height: 20px;" version="1.1" viewbox="0 0 100 100" width="100px" x="0px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" y="0px">
            <g>
            <path d="M78.016,49.132L51.961,12.714c-0.471-0.66-1.233-1.049-2.043-1.051c-0.006,0-0.006,0-0.006,0
                                            c-0.815,0.002-1.575,0.396-2.048,1.059L21.977,49.14c-0.546,0.767-0.616,1.776-0.183,2.612c0.426,0.835,1.292,1.361,2.236,1.361
                                            h12.183l-0.001,32.709c0,1.39,1.125,2.515,2.516,2.515l22.541-0.001c1.389,0.001,2.515-1.124,2.516-2.517l0-32.705h12.187
                                            c0.94,0,1.803-0.53,2.237-1.367C78.641,50.911,78.566,49.9,78.016,49.132z"></path>
            </g>
            </svg>
            </a>
            <div class="tm-login" id="login" onclick="tmEvent('login','click','sign_in_button');
            ">
            <svg class="tm-login__image" enable-background="new 0 0 100 100" fill="#FFF" height="100px" id="Layer_1" version="1.1" viewbox="0 0 100 100" width="100px" x="0px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" y="0px">
            <g>
            <path d="M80.161,60.441l-15.66-7.47l-6.622-3.159c2.892-1.822,5.241-4.634,6.778-8.022c1.22-2.69,1.946-5.734,1.946-8.99
                            c0-1.827-0.29-3.562-0.694-5.236C63.94,19.453,57.605,13.477,50,13.477c-7.461,0-13.701,5.763-15.792,13.645
                            c-0.482,1.808-0.815,3.688-0.815,5.68c0,3.459,0.808,6.684,2.181,9.489c1.587,3.254,3.94,5.937,6.804,7.662l-6.342,2.953
                            l-16.168,7.53c-1.404,0.658-2.327,2.242-2.327,4.011v15.062v2.703c0,2.381,1.659,4.312,3.708,4.312h57.505
                            c2.048,0,3.708-1.93,3.708-4.312v-2.703V64.446C82.46,62.683,81.552,61.114,80.161,60.441z"></path>
            </g>
            </svg>
            <span class="tm-login__cta">
                    Log in    </span>
            </div>
            </nav>
            <div class="quick-select-wrapper">
            <div class="ssc" id="quickselect-skeleton" style="height: 40px;">
            <div class="ssc-wrapper flex" style="height: 100%; padding: 0">
            <div class="ssc-square quickselect-element" style="width: 40px;"></div>
            <div class="ssc-square quickselect-element quickselect-selector" style="width: 171.06px;"></div>
            <div class="ssc-square quickselect-element quickselect-selector" style="width: 170.84px;"></div>
            <div class="ssc-square quickselect-element quickselect-selector" style="width: 138.03px;"></div>
            <div class="ssc-square quickselect-element quickselect-selector" style="width: 141.5px;"></div>
            </div>
            </div>
            <tm-quick-select-bar default-club="27" default-competition="L1" default-country="40" default-player="58358" dropdown-visible="" translations='{"home":"Home","country":"Country","competition":"Competition","club":"club","player":"player","attack":"attack","midfield":"midfield","defense":"defence","goalkeeper":"goalkeeper"}'>
            </tm-quick-select-bar>
            </div>
            <div class="werbung werbung-billboard"><!-- /22272936144,58778164/display_thirdparty/transfermarkt_uk/ros/top_banner -->
            <div id="div-gpt-ad-top_banner" style="min-width: 728px; min-height: 90px;"></div>
            <!-- End AdSlot 2 --></div> </header>
            <main>
            <div aria-hidden="true" class="modal micromodal-slide" id="modal-1" tabindex="1">
            <div class="modal__overlay" data-custom-close="" tabindex="-1">
            <div aria-labelledby="modal-1-title" aria-modal="true" class="modal__container" data-custom-close="" role="dialog">
            <header class="modal__header">
            <button aria-label="Close modal" class="modal__close" data-custom-close=""></button>
            </header>
            <div class="modal__content" id="modal-1-content">
            <img alt="Thomas Müller" data-custom-close="" loading="lazy" src="https://img.a.transfermarkt.technology/portrait/big/58358-1667830486.jpg?lm=1" title="Thomas Müller"/>
            </div>
            </div>
            </div>
            </div>
            <header class="data-header" itemscope="" itemtype="https://schema.org/Person">
            <div class="data-header__headline-container">
            <h1 class="data-header__headline-wrapper">
            <span class="data-header__shirt-number">
                                    #25                    </span>
                                            Thomas <strong>Müller</strong> </h1>
            </div>
            <div class="data-header__badge-container">
            <a class="data-header__success-data" href="/thomas-muller/erfolge/spieler/58358" title="Top goal scorer">
            <img alt="Top goal scorer" class="data-header__success-image lazy lazy" data-src="https://tmssl.akamaized.net/images/titel/header/5.png?lm=1465908312" src="data:image/gif;base64,R0lGODlhAQABAIAAAMLCwgAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" title="Top goal scorer"> <span class="data-header__success-number">3</span>
            </img></a>
            <a class="data-header__success-data" href="/thomas-muller/erfolge/spieler/58358" title="World Cup winner">
            <img alt="World Cup winner" class="" src="https://tmssl.akamaized.net/images/erfolge/header/101.png?lm=1520606996" title="World Cup winner"> <span class="data-header__success-number">1</span>
            </img></a>
            <a class="data-header__success-data" href="/thomas-muller/erfolge/spieler/58358" title="FIFA Club World Cup winner">
            <img alt="FIFA Club World Cup winner" class="" src="https://tmssl.akamaized.net/images/erfolge/header/318.png?lm=1520606999" title="FIFA Club World Cup winner"/> <span class="data-header__success-number">2</span>
            </a>
            <a class="data-header__success-data" href="/thomas-muller/erfolge/spieler/58358" title="Champions League winner">
            <img alt="Champions League winner" class="" src="https://tmssl.akamaized.net/images/erfolge/header/4.png?lm=1520606999" title="Champions League winner"/> <span class="data-header__success-number">2</span>
            </a>
            <a class="data-header__success-data" href="/thomas-muller/erfolge/spieler/58358" title="German Champion">
            <img alt="German Champion" class="" src="https://tmssl.akamaized.net/images/erfolge/header/10.png?lm=1520606996" title="German Champion"/> <span class="data-header__success-number">11</span>
            </a>
            <a href="/thomas-muller/erfolge/spieler/58358" title="All titles &amp; victories">
            <div class="data-header__success-data">
            <span class="data-header__success-more">
            <img src="/images/icons/mehr_erfolge.png"/>
            </span>
            </div>
            </a>
            </div>
            <div class="data-header__box--big">
            <a class="data-header__box__club-link" href="/bayern-munich/startseite/verein/27">
            <img alt="Bayern Munich" height="100" srcset="
                                        https://tmssl.akamaized.net/images/wappen/normquad/27.png?lm=1498251238 1x,
                                        https://tmssl.akamaized.net/images/wappen/homepageWappen150x150/27.png?lm=1498251238 2x
                                        " width="100"/>
            </a>
            <div class="data-header__club-info">
            <span class="data-header__club" itemprop="affiliation">
            <a href="/fc-bayern-munchen/startseite/verein/27" title="Bayern Munich">Bayern Munich</a> </span><br/>
            <span class="data-header__league">
            <a class="data-header__league-link" href="/bundesliga/startseite/wettbewerb/L1">
            <img alt="Bundesliga" class="" src="https://tmssl.akamaized.net/images/logo/verytiny/l1.png?lm=1525905518" title="Bundesliga"/>Bundesliga                                </a>
            </span>
            <span class="data-header__label">League level:
                                            <span class="data-header__content">
            <img alt="Germany" class="flaggenrahmen" src="https://tmssl.akamaized.net/images/flagge/tiny/40.png?lm=1520612525" title="Germany"/>First Tier                                </span>
            </span>
            <span class="data-header__label">Joined: <span class="data-header__content">Jul 1, 2009</span></span>
            <span class="data-header__label">Contract expires: <span class="data-header__content">Jun 30, 2024</span></span>
            </div>
            </div>
            <div class="data-header__profile-container">
            <div class="modal-trigger" data-custom-open="modal-1" id="fotoauswahlOeffnen" onclick="tmEvent('spielerprofil','click','profilbild');" style="cursor:pointer">
            <img alt="Thomas Müller" class="data-header__profile-image" height="181" src="https://img.a.transfermarkt.technology/portrait/header/58358-1667830486.jpg?lm=1" title="Thomas Müller" width="139"/><div class="bildquelle"><span title="IMAGO">IMAGO</span></div>
            <span class="modal-trigger-icon">+</span>
            </div>
            </div>
            <div class="data-header__info-box">
            <div class="data-header__details">
            <ul class="data-header__items">
            <li class="data-header__label">Date of birth/Age:
                                        <span class="data-header__content" itemprop="birthDate">
                                            Sep 13, 1989                                                                    (33)
                                                                        </span>
            </li>
            <li class="data-header__label">Place of birth:
                                            <img alt="Germany" class="flaggenrahmen" src="https://tmssl.akamaized.net/images/flagge/tiny/40.png?lm=1520612525" title="Germany"/> <span class="data-header__content" itemprop="birthPlace">
            <span class="cp" title="Weilheim in Oberbayern">Weilheim in ...</span> </span>
            </li>
            <li class="data-header__label">Citizenship:
                                        <span class="data-header__content" itemprop="nationality">
            <img alt="Germany" class="flaggenrahmen" src="https://tmssl.akamaized.net/images/flagge/tiny/40.png?lm=1520612525" title="Germany"/>                                Germany                            </span>
            </li>
            </ul>
            <ul class="data-header__items">
            <li class="data-header__label">Height:
                                        <span class="data-header__content" itemprop="height">1,85 m</span>
            </li>
            <li class="data-header__label">Position:
                                    <span class="data-header__content">
                                        Second Striker                        </span>
            </li>
            </ul>
            <ul class="data-header__items">
            <li class="data-header__label" for="">
                                                                        Current international:
                                                                    <span class="data-header__content">
            <img alt="Germany" class="flaggenrahmen flagge" src="https://tmssl.akamaized.net/images/flagge/tiny/40.png?lm=1520612525" title="Germany"/><a href="/deutschland/startseite/verein/3262" title="Germany">Germany</a> </span>
            </li>
            <li class="data-header__label">Caps/Goals:
                                            <a class="data-header__content data-header__content--highlight" href="/thomas-muller/nationalmannschaft/spieler/58358/verein_id/3262">118                                </a>/
                                            <a class="data-header__content data-header__content--highlight" href="/thomas-muller/nationalmannschaft/spieler/58358/verein_id/3262">44                                </a>
            </li>
            </ul>
            </div>
            </div>
            <div class="data-header__box--small">
            <a class="data-header__market-value-wrapper" href="/thomas-muller/marktwertverlauf/spieler/58358"><span class="waehrung">€</span>22.00<span class="waehrung">m</span> <p class="data-header__last-update">Last update: Jun 9, 2022</p></a>
            </div>
            </header>
            <a class="db mt10" href="https://www.transfermarkt.co.uk/premier-league-market-values-haaland-knocks-mbappe-off-his-throne-saka-surpasses-salah/view/news/413178" onclick="tmEvent('banner', 'https://www.transfermarkt.co.uk/premier-league-market-values-haaland-knocks-mbappe-off-his-throne-saka-surpasses-salah/view/news/413178', 'd-day-banner');">
            <img alt="deadline-day banner" height="99" src="https://dzjovqk3zamsg.cloudfront.net/MVU_Banner_Premier-League_1122_Desktop_EN.jpg" width="1034"/>
            </a>
            <div class="row hide-on-print" data-action="profil" data-controller="spieler" data-id="58358" data-path="thomas-muller/profil/spieler/58358" data-season="" id="subnavi">
            <div class="page_wrapper subnavi">
            <div class="large-12 columns">
            <div class="subnavi_box" id="subnavigation">
            <div class="submenu-text show-for-small">
            <a name="SubNavi" title="Navigation">
            <span>≡ Sub Menu</span>
            </a>
            </div>
            <nav>
            <ul id="submenu">
            <li class="show-for-small" id="close_submenu">
            <div id="submenu-icon">
            <span class="clicked"></span>
            <span class="clicked"></span>
            </div>
            <a>Close Menu</a>
            </li>
            <li class="first-button aktiv" data-nav-group="profile" id="profile">
            <a class="tm-subnav-item megamenu" href="/thomas-muller/profil/spieler/58358" name="SubNavi" onclick="tmEvent('subnavigation_spieler','click','profil');
            ">Profile</a>
            </li>
            <li class="" data-nav-group="stats" id="stats">
            <a class="tm-subnav-item megamenu_drop" href="#subnavi" name="SubNavi" onclick="tmEvent('subnavigation_spieler','click','leistungsdaten');
            ">Stats</a>
            <div class="dropdown_fullwidth" title=""><div><img class="navigation-loading-spinner" height="40" src="https://tmsi.akamaized.net/icons/tm_spinner_inverted.min.svg" width="40"/></div></div> </li>
            <li class="" data-nav-group="market-value" id="market-value">
            <a class="tm-subnav-item megamenu" href="/thomas-muller/marktwertverlauf/spieler/58358" name="SubNavi" onclick="tmEvent('subnavigation_spieler','click','marktwert');
            ">Market value</a>
            </li>
            <li class="" data-nav-group="transfers" id="transfers">
            <a class="tm-subnav-item megamenu" href="/thomas-muller/transfers/spieler/58358" name="SubNavi" onclick="tmEvent('subnavigation_spieler','click','transfers');
            ">Transfers</a>
            </li>
            <li class="" data-nav-group="rumours" id="rumours">
            <a class="tm-subnav-item megamenu" href="/thomas-muller/geruechte/spieler/58358" name="SubNavi" onclick="tmEvent('subnavigation_spieler','click','geruchte');
            ">Rumours</a>
            </li>
            <li class="" data-nav-group="national-team" id="national-team">
            <a class="tm-subnav-item megamenu" href="/thomas-muller/nationalmannschaft/spieler/58358" name="SubNavi" onclick="tmEvent('subnavigation_spieler','click','nationalmannschaft');
            ">National team</a>
            </li>
            <li class="" data-nav-group="news" id="news">
            <a class="tm-subnav-item megamenu" href="/thomas-muller/news/spieler/58358" name="SubNavi" onclick="tmEvent('subnavigation_spieler','click','news');
            ">News</a>
            </li>
            <li class="" data-nav-group="achievements" id="achievements">
            <a class="tm-subnav-item megamenu" href="/thomas-muller/erfolge/spieler/58358" name="SubNavi" onclick="tmEvent('subnavigation_spieler','click','erfolge');
            ">Achievements</a>
            </li>
            <li class="" data-nav-group="career" id="career">
            <a class="tm-subnav-item megamenu_drop" href="#subnavi" name="SubNavi" onclick="tmEvent('subnavigation_spieler','click','karriere');
            ">Career</a>
            <div class="dropdown_fullwidth" title=""><div><img class="navigation-loading-spinner" height="40" src="https://tmsi.akamaized.net/icons/tm_spinner_inverted.min.svg" width="40"/></div></div> </li>
            <li class="subnavi-edit" data-nav-group="subnavi-edit" id="subnavi-edit">
            <a class="tm-subnav-item megamenu_drop" href="#subnavi" name="SubNavi" onclick="tmEvent('subnavigation_spieler','click','edit');
            "></a>
            <div class="dropdown_fullwidth gasthinweis" title="Log in or register now"><div><img class="navigation-loading-spinner" height="40" src="https://tmsi.akamaized.net/icons/tm_spinner_inverted.min.svg" width="40"/></div></div> </li>
            </ul>
            </nav>
            </div>
            </div>
            </div>
            </div>
            <script>
                    var stickySubTop = $('#subnavigation').offset().top;
                    stickySubTop = stickySubTop - 60;
                    var main = $("#main");
                    $(document).ready(function () {
                        $(window).on('scroll load', function () {
                            if (!main.hasClass("stickySubnavigation")) {
                                stickySubTop = $('#subnavigation').offset().top;
                            }
                            if ($(window).scrollTop() > stickySubTop) {
                                main.addClass("stickySubnavigation");
                            } else {
                                main.removeClass("stickySubnavigation");
                            }
                        });
                    });
                </script>
            <style>
                    .forum-anchor {
                        margin-top: -80px;
                    }
                </style>
            <div class="row">
            <div class="large-8 columns">
            <div class="box tm-player-performance" data-competition-id="L1" data-has-gallery="1" data-player-id="58358" data-skeleton-id="svelte-performance-data--1945728074" data-translations='{"performanceDataButton":"Performance Data","galleryButton":"Gallery ","possibleGames":"Statistics","possibleGame":" Statistics","games":"Appearances","goals":"Goals","assists":"Assists","yellowCard":"Yellow card","yellowCards":"Yellow Cards","secondYellowCard":"Second yellow card","secondYellowCards":"Second Yellows","redCard":"Red card","redCards":"Red cards","startEleven":"Starting eleven","minutesPlayed":"Minutes","goalsContributed":"Goal participation","detailedStatsLink":"Detailed performance data","cleanSheets":"Clean Sheets","goalsConceded":"Goals conceded","performanceSeason":"Performance data :saison","blockedPenaltyPercent":"Penalty Saves"}' id="svelte-performance-data" style="display: none">
            </div>
            <div class="box" id="svelte-performance-data--1945728074">
            <div class="ssc-square" style="width: 100%; height: 292px; border: 5px solid white;"></div>
            </div>
            <script defer="" src="https://tmsi.akamaized.net/js/svelte-performance-data-ce/player-performance-stage.js"></script><script defer="" src="https://tmsi.akamaized.net/js/svelte-performance-data-ce/player-performance-table.js"></script><div class="box viewport-tracking" data-viewport="Steckbrief">
            <h2 class="content-box-headline">Player data </h2>
            <div class="row collapse">
            <div class="large-6 large-push-6 small-12 columns">
            <div class="weitere-daten-spielerprofil">
            <span class="content-box-subheadline">Pronunciation</span>
            <div class="tm-player-pronunciation">
            <audio controls="" id="audio_aussprache" name="audio_58358" preload="none">
            <source src="https://tmssl.akamaized.net/static/audio/spieler/58358.MP3" type="audio/mpeg"/>
            </audio>
            <span class="tm-player-audio-info">
            <a href="https://internationalassociationfootball.wordpress.com/nameproject-uefa-euro-2016/" target="_blank" title="Infos on the pronunciation tool">
            <img src="/images/info.png"/>
            </a>
            </span>
            <br class="clearer"/>
            </div>
            </div>
            <div class="weitere-daten-spielerprofil">
            <span class="content-box-subheadline">
                                    Main position                    </span>
            <div class="detail-position">
            <div class="detail-position__box">
            <div class="detail-position__inner-box">
            <dl>
            <dt class="detail-position__title">Main position:</dt>
            <dd class="detail-position__position">Second Striker</dd>
            </dl>
            </div>
            <div class="detail-position__position">
            <dl>
            <dt class="detail-position__title">Other position:</dt>
            <dd class="detail-position__position">Attacking Midfield</dd>
            <dd class="detail-position__position">Right Winger</dd>
            </dl>
            </div>
            </div>
            <div class="detail-position__matchfield">
            <span class="position position__primary position__primary--13"></span>
            <span class="position position__secondary position__secondary--10"></span>
            <span class="position position__secondary position__secondary--12"></span>
            </div>
            </div>
            <div class="box viewport-tracking tm-player-market-value-development-container" data-viewport="Marktwert">
            <div class="content-box-subheadline"><span>Market value</span></div>
            <div class="tm-player-market-value-development">
            <div class="tm-player-market-value-development__current-and-max">
            <div>
            <div>Current market value:</div>
            <div class="tm-player-market-value-development__current-value">
                            €22.00m                </div>
            </div>
            <div class="tm-player-market-value-development__max">
            <div>Highest market value:</div>
            <div class="tm-player-market-value-development__max-value">€75.00m</div>
            <div>Oct 16, 2015</div>
            </div>
            </div>
            <div class="tm-player-market-value-development__graph">
            <a href="/thomas-muller/marktwertverlauf/spieler/58358">
            <div id="yw0"></div> </a>
            </div>
            <div class="tm-player-market-value-development__update">
                        Last update: Jun 9, 2022        </div>
            </div>
            <a class="content-link" href="/thomas-muller/marktwertverlauf/spieler/58358">Market value details</a>
            </div>
            </div>
            </div>
            <div class="large-6 large-pull-6 small-12 columns spielerdatenundfakten">
            <span class="content-box-subheadline show-for-small">
                            Facts and data            </span>
            <div class="info-table info-table--right-space min-height-audio">
            <span class="info-table__content info-table__content--regular">Date of birth:</span>
            <span class="info-table__content info-table__content--bold"><a href="/aktuell/waspassiertheute/aktuell/new/datum/1989-09-13">Sep 13, 1989</a> </span>
            <span class="info-table__content info-table__content--regular">Place of birth:</span>
            <span class="info-table__content info-table__content--bold">
            <span>Weilheim in Oberbayern  <img alt="Germany" class="flaggenrahmen lazy lazy" data-src="https://tmssl.akamaized.net/images/flagge/tiny/40.png?lm=1520612525" src="data:image/gif;base64,R0lGODlhAQABAIAAAMLCwgAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" title="Germany"/></span> </span>
            <span class="info-table__content info-table__content--regular">Age:</span>
            <span class="info-table__content info-table__content--bold">33</span>
            <span class="info-table__content info-table__content--regular">Height:</span>
            <span class="info-table__content info-table__content--bold">1,85 m</span>
            <span class="info-table__content info-table__content--regular">Citizenship:</span>
            <span class="info-table__content info-table__content--bold">
            <img alt="Germany" class="flaggenrahmen" src="https://tmssl.akamaized.net/images/flagge/tiny/40.png?lm=1520612525" title="Germany"/>  Germany                            </span>
            <span class="info-table__content info-table__content--regular">Position:</span>
            <span class="info-table__content info-table__content--bold">
                                        Attack - Second Striker                        </span>
            <span class="info-table__content info-table__content--regular">Foot:</span>
            <span class="info-table__content info-table__content--bold">right</span>
            <span class="info-table__content info-table__content--regular">Player agent:</span>
            <span class="info-table__content info-table__content--bold info-table__content--flex">
            <a href="/kogl-amp-partner-gmbh/beraterfirma/berater/302">Kögl &amp; Partner GmbH</a> </span>
            <span class="info-table__content info-table__content--regular">
                                        Current club:
                                    </span>
            <span class="info-table__content info-table__content--bold info-table__content--flex">
            <a href="/bayern-munich/startseite/verein/27">
            <img alt="Bayern Munich" height="15" srcset="https://tmssl.akamaized.net/images/wappen/small/27.png?lm=1498251238 1x,
                                                        https://tmssl.akamaized.net/images/wappen/homepage/27.png?lm=1498251238 2x" width="15"/>
            </a>
            <a href="/fc-bayern-munchen/startseite/verein/27" title="Bayern Munich">Bayern Munich</a> </span>
            <span class="info-table__content info-table__content--regular">Joined:</span>
            <span class="info-table__content info-table__content--bold">
                                            Jul 1, 2009                            </span>
            <span class="info-table__content info-table__content--regular">Contract expires:</span>
            <span class="info-table__content info-table__content--bold">Jun 30, 2024</span>
            <span class="info-table__content info-table__content--regular info-table__span--line-height">Date of last contract extension:</span>
            <span class="info-table__content info-table__content--bold info-table__span--specific">May 3, 2022</span>
            <span class="info-table__content info-table__content--regular">Outfitter:</span>
            <span class="info-table__content info-table__content--bold">adidas</span>
            <span class="info-table__content info-table__content--regular">Social-Media:</span>
            <span class="info-table__content info-table__content--bold"><div class="socialmedia-icons">
            <a href="http://twitter.com/esmuellert_" target="_blank" title="Twitter">
            <img class="lazy" data-src="https://tmsi.akamaized.net/icons/twitter.svg" height="20px" width="20px"/> </a>
            <a href="http://www.facebook.com/es.muellert.wieder" target="_blank" title="Facebook">
            <img class="lazy" data-src="https://tmsi.akamaized.net/icons/facebook.svg" height="20px" width="20px"/> </a>
            <a href="http://www.instagram.com/esmuellert/" target="_blank" title="Instagram">
            <img class="lazy" data-src="https://tmsi.akamaized.net/icons/instagram.svg" height="20px" width="20px"/> </a>
            <a href="http://www.esmuellertwieder.de/" target="_blank" title="">
            <img class="lazy" data-src="https://tmsi.akamaized.net/icons/.svg" height="20px" width="20px"/> </a>
            <a href="http://www.tiktok.com/@esmuellert" target="_blank" title="TikTok">
            <img class="lazy" data-src="https://tmsi.akamaized.net/icons/tiktok.svg" height="20px" width="20px"/> </a>
            </div>
            </span>
            </div>
            </div>
            </div>
            </div>
            <div class="werbung werbung-ADTAG_CONTENT_BODY_1"><!-- /22272936144,58778164/display_thirdparty/transfermarkt_uk/ros/skin -->
            <div id="div-gpt-ad-skin" style="min-width: 1px; min-height: 1px;"></div>
            <!-- End AdSlot 5 --></div><div class="verletzungsbox">
            <div class="verletzt">
            <img src="/images/icons/verletzt.png"/>
            </div>
            <div class="text">
                    Hip problems<br/><span class="rueckkehr">Return expected on Nov 13, 2022</span> </div>
            </div>
            <div class="box viewport-tracking" data-viewport="Transferhistorie">
            <h2 class="content-box-headline">
                    Transfer history     </h2>
            <div class="grid tm-player-transfer-history-grid tm-player-transfer-history-grid tm-player-transfer-history-grid--heading">
            <div class="grid__heading grid__heading--center tm-player-transfer-history-grid__season">Season</div>
            <div class="grid__heading grid__heading--center tm-player-transfer-history-grid__date">Date</div>
            <div class="grid__heading tm-player-transfer-history-grid__old-club">Left</div>
            <div class="grid__heading tm-player-transfer-history-grid__new-club">Joined</div>
            <div class="grid__heading grid__heading--ar tm-player-transfer-history-grid__market-value">MV</div>
            <div class="grid__heading grid__heading--ar tm-player-transfer-history-grid__fee">Fee</div>
            <span class="grid__heading tm-player-transfer-history-grid__link--placeholder"></span>
            </div>
            <div class="grid tm-player-transfer-history-grid">
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__season">
                                        09/10                    </div>
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__date">
                        Jul 1, 2009        </div>
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__old-club">
            <a href="/fc-bayern-munich-ii/transfers/verein/28/saison_id/2009">
            <img alt="FC Bayern II" class="tm-player-transfer-history-grid__club-logo lazy" data-srcset="
                                    https://tmssl.akamaized.net/images/wappen/tiny/27_1498251266.png?lm=1498251266 1x,
                                    https://tmssl.akamaized.net/images/wappen/smallquad/27_1498251266.png?lm=1498251266 2x
                                " height="15" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" width="15"/>
            </a>
            <img alt="" class="tm-player-transfer-history-grid__flag lazy" data-src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
            <a class="tm-player-transfer-history-grid__club-link" href="/fc-bayern-munich-ii/transfers/verein/28/saison_id/2009">
                                        FC Bayern II                            </a>
            </div>
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__new-club">
            <a href="/bayern-munich/transfers/verein/27/saison_id/2009">
            <img alt="Bayern Munich" class="tm-player-transfer-history-grid__club-logo lazy" data-srcset="
                                    https://tmssl.akamaized.net/images/wappen/tiny/27_1498251266.png?lm=1498251266 1x,
                                    https://tmssl.akamaized.net/images/wappen/smallquad/27_1498251266.png?lm=1498251266 2x
                                " height="15" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" width="15">
            </img></a>
            <img alt="" class="tm-player-transfer-history-grid__flag lazy" data-src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
            <a class="tm-player-transfer-history-grid__club-link" href="/bayern-munich/transfers/verein/27/saison_id/2009">
                                        Bayern Munich                            </a>
            </div>
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__market-value">
                        €750k        </div>
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__fee">
                                    -                    </div>
            <a class="grid__cell grid__cell--center tm-player-transfer-history-grid__link" href="/thomas-muller/transfers/spieler/58358/transfer_id/269886">
            </a>
            </div>
            <div class="grid tm-player-transfer-history-grid">
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__season">
                                        08/09                    </div>
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__date">
                        Jul 1, 2008        </div>
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__old-club">
            <a href="/fc-bayern-munich-u19/transfers/verein/1462/saison_id/2008">
            <img alt="FC Bayern U19" class="tm-player-transfer-history-grid__club-logo lazy" data-srcset="
                                    https://tmssl.akamaized.net/images/wappen/tiny/27_1498251266.png?lm=1498251266 1x,
                                    https://tmssl.akamaized.net/images/wappen/smallquad/27_1498251266.png?lm=1498251266 2x
                                " height="15" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" width="15">
            </img></a>
            <img alt="" class="tm-player-transfer-history-grid__flag lazy" data-src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
            <a class="tm-player-transfer-history-grid__club-link" href="/fc-bayern-munich-u19/transfers/verein/1462/saison_id/2008">
                                        FC Bayern U19                            </a>
            </div>
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__new-club">
            <a href="/fc-bayern-munich-ii/transfers/verein/28/saison_id/2008">
            <img alt="FC Bayern II" class="tm-player-transfer-history-grid__club-logo lazy" data-srcset="
                                    https://tmssl.akamaized.net/images/wappen/tiny/27_1498251266.png?lm=1498251266 1x,
                                    https://tmssl.akamaized.net/images/wappen/smallquad/27_1498251266.png?lm=1498251266 2x
                                " height="15" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" width="15">
            </img></a>
            <img alt="" class="tm-player-transfer-history-grid__flag lazy" data-src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
            <a class="tm-player-transfer-history-grid__club-link" href="/fc-bayern-munich-ii/transfers/verein/28/saison_id/2008">
                                        FC Bayern II                            </a>
            </div>
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__market-value">
                        -        </div>
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__fee">
                                    -                    </div>
            <a class="grid__cell grid__cell--center tm-player-transfer-history-grid__link" href="/thomas-muller/transfers/spieler/58358/transfer_id/753582">
            </a>
            </div>
            <div class="grid tm-player-transfer-history-grid">
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__season">
                                        06/07                    </div>
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__date">
                        Jul 1, 2006        </div>
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__old-club">
            <a href="/fc-bayern-munich-u17/transfers/verein/21058/saison_id/2006">
            <img alt="FC Bayern U17" class="tm-player-transfer-history-grid__club-logo lazy" data-srcset="
                                    https://tmssl.akamaized.net/images/wappen/tiny/27_1498251266.png?lm=1498251266 1x,
                                    https://tmssl.akamaized.net/images/wappen/smallquad/27_1498251266.png?lm=1498251266 2x
                                " height="15" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" width="15">
            </img></a>
            <img alt="" class="tm-player-transfer-history-grid__flag lazy" data-src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
            <a class="tm-player-transfer-history-grid__club-link" href="/fc-bayern-munich-u17/transfers/verein/21058/saison_id/2006">
                                        FC Bayern U17                            </a>
            </div>
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__new-club">
            <a href="/fc-bayern-munich-u19/transfers/verein/1462/saison_id/2006">
            <img alt="FC Bayern U19" class="tm-player-transfer-history-grid__club-logo lazy" data-srcset="
                                    https://tmssl.akamaized.net/images/wappen/tiny/27_1498251266.png?lm=1498251266 1x,
                                    https://tmssl.akamaized.net/images/wappen/smallquad/27_1498251266.png?lm=1498251266 2x
                                " height="15" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" width="15">
            </img></a>
            <img alt="" class="tm-player-transfer-history-grid__flag lazy" data-src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
            <a class="tm-player-transfer-history-grid__club-link" href="/fc-bayern-munich-u19/transfers/verein/1462/saison_id/2006">
                                        FC Bayern U19                            </a>
            </div>
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__market-value">
                        -        </div>
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__fee">
                                    -                    </div>
            <a class="grid__cell grid__cell--center tm-player-transfer-history-grid__link" href="/thomas-muller/transfers/spieler/58358/transfer_id/663100">
            </a>
            </div>
            <div class="grid tm-player-transfer-history-grid">
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__season">
                                        04/05                    </div>
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__date">
                        Jul 1, 2004        </div>
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__old-club">
            <a href="/fc-bayern-munchen-youth/transfers/verein/18936/saison_id/2004">
            <img alt="B. München Yth." class="tm-player-transfer-history-grid__club-logo lazy" data-srcset="
                                    https://tmssl.akamaized.net/images/wappen/tiny/27_1498251266.png?lm=1498251266 1x,
                                    https://tmssl.akamaized.net/images/wappen/smallquad/27_1498251266.png?lm=1498251266 2x
                                " height="15" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" width="15">
            </img></a>
            <img alt="" class="tm-player-transfer-history-grid__flag lazy" data-src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
            <a class="tm-player-transfer-history-grid__club-link" href="/fc-bayern-munchen-youth/transfers/verein/18936/saison_id/2004">
                                        B. München Yth.                            </a>
            </div>
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__new-club">
            <a href="/fc-bayern-munich-u17/transfers/verein/21058/saison_id/2004">
            <img alt="FC Bayern U17" class="tm-player-transfer-history-grid__club-logo lazy" data-srcset="
                                    https://tmssl.akamaized.net/images/wappen/tiny/27_1498251266.png?lm=1498251266 1x,
                                    https://tmssl.akamaized.net/images/wappen/smallquad/27_1498251266.png?lm=1498251266 2x
                                " height="15" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" width="15">
            </img></a>
            <img alt="" class="tm-player-transfer-history-grid__flag lazy" data-src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
            <a class="tm-player-transfer-history-grid__club-link" href="/fc-bayern-munich-u17/transfers/verein/21058/saison_id/2004">
                                        FC Bayern U17                            </a>
            </div>
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__market-value">
                        -        </div>
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__fee">
                                    -                    </div>
            <a class="grid__cell grid__cell--center tm-player-transfer-history-grid__link" href="/thomas-muller/transfers/spieler/58358/transfer_id/663101">
            </a>
            </div>
            <div class="grid tm-player-transfer-history-grid">
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__season">
                                        00/01                    </div>
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__date">
                        Jul 1, 2000        </div>
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__old-club">
            <a href="/tsv-pahl-youth/transfers/verein/42290/saison_id/2000">
            <img alt="TSV Pähl Yth." class="tm-player-transfer-history-grid__club-logo lazy" data-srcset="
                                    https://tmssl.akamaized.net/images/wappen/tiny/42290.png?lm=1413884650 1x,
                                    https://tmssl.akamaized.net/images/wappen/smallquad/42290.png?lm=1413884650 2x
                                " height="15" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" width="15">
            </img></a>
            <img alt="" class="tm-player-transfer-history-grid__flag lazy" data-src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
            <a class="tm-player-transfer-history-grid__club-link" href="/tsv-pahl-youth/transfers/verein/42290/saison_id/2000">
                                        TSV Pähl Yth.                            </a>
            </div>
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__new-club">
            <a href="/fc-bayern-munchen-youth/transfers/verein/18936/saison_id/2000">
            <img alt="B. München Yth." class="tm-player-transfer-history-grid__club-logo lazy" data-srcset="
                                    https://tmssl.akamaized.net/images/wappen/tiny/18936_1414673804.png?lm=1414673804 1x,
                                    https://tmssl.akamaized.net/images/wappen/smallquad/18936_1414673804.png?lm=1414673804 2x
                                " height="15" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" width="15">
            </img></a>
            <img alt="" class="tm-player-transfer-history-grid__flag lazy" data-src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
            <a class="tm-player-transfer-history-grid__club-link" href="/fc-bayern-munchen-youth/transfers/verein/18936/saison_id/2000">
                                        B. München Yth.                            </a>
            </div>
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__market-value">
                        -        </div>
            <div class="grid__cell grid__cell--center tm-player-transfer-history-grid__fee">
                                    free transfer                    </div>
            <a class="grid__cell grid__cell--center tm-player-transfer-history-grid__link" href="/thomas-muller/transfers/spieler/58358/transfer_id/977308">
            </a>
            </div>
            <div class="grid__footer grid__footer--dark player-transfer-history__footer-container tm-player-transfer-history-grid tm-player-transfer-history-grid--sum tm-player-transfer-history-grid--heading">
            <div class="tm-player-transfer-history-grid__hint">Total transfer fees:</div>
            <div class="tm-player-transfer-history-grid__fee">0</div>
            <span></span>
            </div>
            </div>
            <div class="box tm-player-additional-data viewport-tracking" data-viewport="Jugendvereine">
            <span class="content-box-headline">
                            Youth clubs            </span>
            <div class="content">
                                    TSV Pähl (1993-2000), FC Bayern München (2000-2008)        </div>
            </div>
            <div class="werbung werbung-ADTAG_CONTENT_BODY_2"><!-- /22272936144,58778164/display_thirdparty/transfermarkt_uk/ros/high_impact -->
            <div id="div-gpt-ad-high_impact" style="min-width: 1px; min-height: 1px;"></div>
            <!-- End AdSlot 6 --></div><div class="box"><script async="" src="https://fcp.codes/embed-code-template/embed-code-template.js#SMART_91f60932-b199-4dbc-8630-16ac5e06b884"></script>
            </div> <div class="box viewport-tracking">
            <h2 class="content-box-headline">
                        Stats of Thomas Müller         </h2>
            <div data-player-id="58358" data-translations='{"games":"Appearances","goals":"Goals","assists":"Assists","minutesPlayed":"Minutes","detailedStatsLink":"Detailed performance data","cleanSheets":"Clean Sheets","goalsConceded":"Goals conceded","minutesPerGoal":"Minutes per goal","sum":"Total ","competition":"Competition"}' id="player-performance-table"></div>
            <a class="content-link" href="/thomas-muller/leistungsdaten/spieler/58358">View full stats</a>
            </div>
            <div class="box" id="recommender">
            <div class="OUTBRAIN" data-ob-template="DE_Transfermarkt.de" data-src="" data-widget-id="AR_1"></div>
            <script src="https://widgets.outbrain.com/outbrain.js" type="text/javascript"></script>
            </div>
            </div>
            <div class="large-4 columns">
            <div class="next-matches-skeleton" id="tm-next-matches-1907835079">
            <div class="ssc-square skeleton-table-header"></div>
            <div class="skeleton-flex-c skeleton-flex-col skeleton-h-var" style="--tm-skeleton-height: 70px;">
            <div class="ssc-square skeleton-hw-var skeleton-mb-2" style="--tm-skeleton-height: 14px; --tm-skeleton-width: 145px;"></div>
            <div class="ssc-square skeleton-hw-var" style="--tm-skeleton-height: 14px; --tm-skeleton-width: 100px;"></div>
            </div>
            <div class="skeleton-flex-align-center skeleton-flex-justify-evenly skeleton-h-var skeleton-mlr-20" style="--tm-skeleton-height: 80px;">
            <div class="skeleton-flex-align-center skeleton-flex-col">
            <div class="ssc-circle skeleton-hw-var" style="--tm-skeleton-height: 50px; --tm-skeleton-width: 50px"></div>
            <div class="ssc-square skeleton-hw-var skeleton-mt-10" style="--tm-skeleton-height: 70px; --tm-skeleton-width: 70px;"></div>
            </div>
            <div class="ssc-square skeleton-hw-var" style="--tm-skeleton-height: 20px; --tm-skeleton-width: 40px"></div>
            <div class="skeleton-flex-align-center skeleton-flex-col">
            <div class="ssc-circle skeleton-hw-var" style="--tm-skeleton-height: 50px; --tm-skeleton-width: 50px"></div>
            <div class="ssc-square skeleton-hw-var skeleton-mt-10" style="--tm-skeleton-height: 70px; --tm-skeleton-width: 70px;"></div>
            </div>
            </div>
            <div class="ssc-square" style="height: 20px; width: 240px; margin: 40px auto 10px"></div>
            <div style="display: flex; justify-content: space-between; padding: 0 5px;">
            <div class="ssc-square" style="height: 50px; width: 156px;"></div>
            <div class="ssc-square" style="height: 50px; width: 156px;"></div>
            </div>
            </div>
            <tm-next-matches class="viewport-tracking" data-viewport="Naechste_Begegnungen" identifier="58358" locale="en" skeleton="tm-next-matches-1907835079" translations='{"headline":"Next matches","matchDay":"Matchday"}' type="player">
            <div class="quote-slot" onclick="tmEvent('werbung','click','begegnungsbox_spieler');" slot="quotes">
            <span class="oddsServe" data-competition="0" data-gameday="0" data-match="0"></span> </div>
            </tm-next-matches>
            <script>
                var nextMatchesEl = document.getElementsByTagName('tm-next-matches')[0];
                if(nextMatchesEl) {
                    nextMatchesEl.addEventListener('nextMatchesReloadQuotes', (event) => {
                        jQuery(document).trigger('begegnungenVereinSliderLoad');
                    });
                }
            </script>
            <div class="werbung werbung-rectangle1"><!-- /22272936144,58778164/display_thirdparty/transfermarkt_uk/ros/top_mpu -->
            <div id="div-gpt-ad-top_mpu" style="width: 300px; height: 250px;"></div>
            <!-- End AdSlot 3 --></div><div class="box viewport-tracking" data-viewport="Laenderspielkarriere">
            <h2 class="content-box-headline">National team career</h2>
            <div class="grid">
            <div class="grid national-career__row national-career__row--header">
            <div class="grid__heading grid__heading--center">
                            #            </div>
            <div class="grid__heading">
                            National team            </div>
            <div class="grid__heading grid__heading--center">
                            Debut            </div>
            <div class="grid__heading grid__heading--center">
            <img alt="Matches" class="national-career__icon" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0OC41IDYwIiB4bWw6c3BhY2U9InByZXNlcnZlIj48cGF0aCBmaWxsPSIjMUIzMjUxIiBkPSJNNDUuODUgMi41NXY1NC44SDIuNjVWMi41NXoiLz48cGF0aCBmaWxsPSIjRkZGIiBkPSJNNDMuMiA1aC0zOHY1MGgzOFY1ek0zMC40IDMwLjljLS41IDIuOC0yLjkgNS01LjggNXMtNS40LTIuMi01LjgtNWgxMS42ek0zMS4zIDd2Ni4xSDE3LjJWN2gxNC4xek0xOC44IDI5Yy41LTIuOCAyLjktNSA1LjgtNXM1LjQgMi4yIDUuOCA1SDE4Ljh6bTEzLjMgMGMtLjUtMy44LTMuNi02LjctNy41LTYuN3MtNy4xIDIuOS03LjUgNi43SDcuM1Y3aDh2OGgxNy45VjdoOC4xdjIyaC05LjJ6TTcuMyAzMC45aDkuOGMuNSAzLjggMy42IDYuNyA3LjUgNi43czcuMS0yLjkgNy41LTYuN2g5LjJ2MjJoLTguMVY0NUgxNS4zdjcuOWgtOHYtMjJ6bTI0IDIyLjFIMTcuMnYtNmgxNC4xdjZ6Ii8+PC9zdmc+" title="Matches">
            </img></div>
            <div class="grid__heading grid__heading--center">
            <img alt="Goals" class="national-career__icon" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNSAxNSI+PGRlZnM+PHN0eWxlPi5he2ZpbGw6IzFiMzI1MX08L3N0eWxlPjwvZGVmcz48cGF0aCBjbGFzcz0iYSIgZD0iTTE1IDcuNUE3LjUgNy41IDAgMSAxIDcuNSAwIDcuNDkgNy40OSAwIDAgMSAxNSA3LjVaIi8+PGNpcmNsZSBjeD0iNi40MjUiIGN5PSI2LjQyNSIgcj0iNi40MjUiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuMDc1IDEuMDc1KSIgc3R5bGU9ImZpbGw6I2ZmZiIvPjxwYXRoIGNsYXNzPSJhIiBkPSJtNS44IDYuOTc1LjY1IDJoMi4xbC42NS0yTDcuNSA1Ljc1Wm0xLjctNC44QTUuMzI1IDUuMzI1IDAgMSAwIDEyLjgyNSA3LjUgNS4zMTMgNS4zMTMgMCAwIDAgNy41IDIuMTc1Wm0xLjg1IDcuODc1LS42IDEuOWE1LjAyOSA1LjAyOSAwIDAgMS0xLjI1LjE3NSA1LjIgNS4yIDAgMCAxLTEuMjUtLjE3NWwtLjYyNS0xLjloLTJhNC43ODUgNC43ODUgMCAwIDEtLjc3NS0yLjM3NUw0LjQ1IDYuNWwtLjYyNS0xLjlBNC41MzQgNC41MzQgMCAwIDEgNS44NSAzLjE1bDEuNiAxLjE3NSAxLjYtMS4xNzVhNC43MzMgNC43MzMgMCAwIDEgMi4wMjUgMS40NUwxMC41IDYuNTI1IDEyLjEgNy43YTQuNDA2IDQuNDA2IDAgMCAxLS43NzUgMi4zNzVIOS4zNVoiLz48L3N2Zz4=" title="Tore "/>
            </div>
            </div>
            <div class="grid national-career__row">
            <div class="grid__cell grid__cell--center national-career__cell--green">
                                13                </div>
            <div class="grid__cell grid__cell--club">
            <img alt="Germany" class="flaggenrahmen lazy lazy" data-src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" src="data:image/gif;base64,R0lGODlhAQABAIAAAMLCwgAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" title="Germany"/><a href="/deutschland/startseite/verein/3262" title="Germany">Germany</a> </div>
            <div class="grid__cell grid__cell--center">
            <a href="/spiel/index/spielbericht/982185">Mar 3, 2010</a>
            </div>
            <div class="grid__cell grid__cell--center">
            <a href="/thomas-muller/nationalmannschaft/spieler/58358/verein_id/3262">118</a>
            </div>
            <div class="grid__cell grid__cell--center">
            <a href="/thomas-muller/nationalmannschaft/spieler/58358/verein_id/3262/nurEinsatz/2">44</a>
            </div>
            </div>
            <div class="grid national-career__row">
            <div class="grid__cell grid__cell--center national-career__cell--red">
                                13                </div>
            <div class="grid__cell grid__cell--club">
            <img alt="Germany" class="flaggenrahmen lazy lazy" data-src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" src="data:image/gif;base64,R0lGODlhAQABAIAAAMLCwgAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" title="Germany"/><a href="/deutschland-u21/startseite/verein/3817" title="Germany U21">Germany U21</a> </div>
            <div class="grid__cell grid__cell--center">
            <a href="/spiel/index/spielbericht/972005">Aug 11, 2009</a>
            </div>
            <div class="grid__cell grid__cell--center">
            <a href="/thomas-muller/nationalmannschaft/spieler/58358/verein_id/3817">6</a>
            </div>
            <div class="grid__cell grid__cell--center">
            <a href="/thomas-muller/nationalmannschaft/spieler/58358/verein_id/3817/nurEinsatz/2">1</a>
            </div>
            </div>
            <div class="grid national-career__row">
            <div class="grid__cell grid__cell--center national-career__cell--red">
                                13                </div>
            <div class="grid__cell grid__cell--club">
            <img alt="Germany" class="flaggenrahmen lazy lazy" data-src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" src="data:image/gif;base64,R0lGODlhAQABAIAAAMLCwgAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" title="Germany"/><a href="/deutschland-u20/startseite/verein/5709" title="Germany U20">Germany U20</a> </div>
            <div class="grid__cell grid__cell--center">
            <a href="/spiel/index/spielbericht/930676">Sep 3, 2008</a>
            </div>
            <div class="grid__cell grid__cell--center">
            <a href="/thomas-muller/nationalmannschaft/spieler/58358/verein_id/5709">1</a>
            </div>
            <div class="grid__cell grid__cell--center">
            <a href="/thomas-muller/nationalmannschaft/spieler/58358/verein_id/5709/nurEinsatz/2">1</a>
            </div>
            </div>
            <div class="grid national-career__row">
            <div class="grid__cell grid__cell--center national-career__cell--red">
                                13                </div>
            <div class="grid__cell grid__cell--club">
            <img alt="Germany" class="flaggenrahmen lazy lazy" data-src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" src="data:image/gif;base64,R0lGODlhAQABAIAAAMLCwgAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" title="Germany"/><a href="/deutschland-u19/startseite/verein/5710" title="Germany U19">Germany U19</a> </div>
            <div class="grid__cell grid__cell--center">
            <a href="/spiel/index/spielbericht/2459236">Nov 14, 2007</a>
            </div>
            <div class="grid__cell grid__cell--center">
            <a href="/thomas-muller/nationalmannschaft/spieler/58358/verein_id/5710">3</a>
            </div>
            <div class="grid__cell grid__cell--center">
            <a href="/thomas-muller/nationalmannschaft/spieler/58358/verein_id/5710/nurEinsatz/2">-</a>
            </div>
            </div>
            <div class="grid national-career__row">
            <div class="grid__cell grid__cell--center national-career__cell--red">
                                13                </div>
            <div class="grid__cell grid__cell--club">
            <img alt="Germany" class="flaggenrahmen lazy lazy" data-src="https://tmssl.akamaized.net/images/flagge/verysmall/40.png?lm=1520612525" src="data:image/gif;base64,R0lGODlhAQABAIAAAMLCwgAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" title="Germany"/><a href="/deutschland-u16/startseite/verein/17368" title="Germany U16">Germany U16</a> </div>
            <div class="grid__cell grid__cell--center">
                                                                            Oct 1, 2004                                                             </div>
            <div class="grid__cell grid__cell--center">
            <a href="/thomas-muller/nationalmannschaft/spieler/58358/verein_id/17368">6</a>
            </div>
            <div class="grid__cell grid__cell--center">
            <a href="/thomas-muller/nationalmannschaft/spieler/58358/verein_id/17368/nurEinsatz/2">-</a>
            </div>
            </div>
            </div>
            <a class="content-link" href="/thomas-muller/nationalmannschaft/spieler/58358">Go to national player profile</a></div>
            <div id="compare-player-skeleton-1178105792" style="margin-top: 10px">
            <div class="ssc-square skeleton-table-header"></div>
            <div style=" display: flex; margin: 5px">
            <div class="ssc-square" style="width: 93px; height: 63px;"></div>
            <div style="margin: 5px">
            <div class="ssc-square" style="width: 200px; height: 26px; margin-bottom: 5px"></div>
            <div class="ssc-square" style="width: 200px; height: 26px"></div>
            </div>
            </div>
            </div>
            <tm-compare-player button-text="Compare players" data-viewport="Vergleiche_mit_" headline="Compare Thomas Müller with ..." id="viewport-tracking" player-full-name="Thomas Müller" player-id="58358" search-player="Search for players" skeleton="compare-player-skeleton-1178105792">
            </tm-compare-player>
            <section class="fav-voting" data-viewport="Beliebtheitsvote">
            <header class="fav-voting__header">
            <h2 class="fav-voting__headline">
                            Whom do you prefer?            </h2>
            <a class="fav-voting__reload-btn" href="" role="button" title="New match">
            <svg fill="none" height="15" viewbox="0 0 14 15" width="14" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
            <rect fill="url(#pattern0)" height="15" width="14"></rect>
            <defs>
            <pattern height="1" id="pattern0" patterncontentunits="objectBoundingBox" width="1">
            <use transform="scale(0.0714286 0.0666667)" xlink:href="#image0_757_2"></use>
            </pattern>
            <image height="15" id="image0_757_2" width="14" xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAPCAYAAADUFP50AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyZpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMDE0IDc5LjE1Njc5NywgMjAxNC8wOC8yMC0wOTo1MzowMiAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTQgKFdpbmRvd3MpIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjZCMjlCNDlGRTQxNjExRTRCQjAyQUVDQTBFMkY0N0FFIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjZCMjlCNEEwRTQxNjExRTRCQjAyQUVDQTBFMkY0N0FFIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6NkIyOUI0OURFNDE2MTFFNEJCMDJBRUNBMEUyRjQ3QUUiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6NkIyOUI0OUVFNDE2MTFFNEJCMDJBRUNBMEUyRjQ3QUUiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz66VzloAAACaUlEQVR42mKULV3MgAwq7VWO33nzxfj1t98s/xkYGAU5mP/KC3A9mXj8gQJMTay+1DcWGKfHWyd96/Xn07uP3GP88/cfslnMQCxvLS/031pO8OLJJx/0ll1+zgjW2OmhVTPn9MPmG68+Q1QyMTLICnCB6ddffjJ8+vGb4ejDdwxATfogQ0V5OBgYNx+9JLTo7KO3Jx6/B2vSkeBjcJAXfC4ryD2PlZnpGlCh+srLz+rOPv0Ad4IkHycDy/UXHy7DNOlL8jPEG8sGF225sg7E7/fRsb/x8tOMx59+oIQD0O8MLBdefJYCcQS42BgCNcW3wjSBwIO3XxatvfGK9xeqnxnef/vFwPLw408wR0OYm6Fh3y0fZAXywjyFVfYqRj9//1V5/fWH7duvv4SffP7F/v3PX7AfJbI2XHzBQAKYFqAvwRg0cfN/ThZmBhletp/C3GxvRbk5DrOzMt9hZWE6h+xsELCQFfwPCg85QW4GlksvPjP8BFoNBOxALMXJxhLOxszEkGAg9QjIh2tscFLbMuHEA4gX+NkZmASBgYIMeNlZGII1xD4rCPPEwcT6fHSC1l9/6f0BGCggYCDB+4yFEc39snwcDBrifP3//zNIAxNGy+P3X5PmnXkkeeXFJ5hzGTQlBHRZ/vz7DxZgAToPlCpAEX377dc6UR52hr9AuccfvoFpcMiL8TIEakvWAgPzHcu7bz8Z7BWF/5vLCFw6+ui9PihpgZIYCMMAyFBbecH/3pqSmSVbr8wEiTFWLdn7bfHFZ1wwRfmWCg8efvgm8/7HX2agN/6LcrH+URHhOdt+8I4lspcAAgwAHaQA7YXnQ28AAAAASUVORK5CYII="/>
            </defs>
            </svg>
            </a>
            </header>
            <div class="fav-voting__content">
            <p class="fav-voting__question fav-voting__question--text-favorite">
                                Which player do you prefer...                </p>
            <div class="fav-voting__wrapper">
            <a class="fav-voting__link-player fav-voting__link-player--red" href="/beliebtheit/speichernSpieler?spieler_id_gewinner=58358&amp;spieler_id_verlierer=344695&amp;kontinent=0&amp;land=0&amp;wettbewerb=L1&amp;verein=27&amp;position=0&amp;marktwert=0&amp;spieler_id_1=58358&amp;lieblingsverein=0">
            <img alt="Thomas Müller" class="lazy" data-src="https://img.a.transfermarkt.technology/portrait/medium/58358-1667830486.jpg?lm=1" src="data:image/gif;base64,R0lGODlhAQABAIAAAMLCwgAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" title="Thomas Müller - source: IMAGO"/> <div class="fav-voting__name">
                                    Thomas Müller                    </div>
            <div class="fav-voting__club fav-voting__club--left">
            <img alt="Bayern Munich" class="" src="https://tmssl.akamaized.net/images/wappen/kaderquad/27.png?lm=1498251238" title="Bayern Munich"/> </div>
            </a>
            <img alt="versus" class="fav-voting__versus-image" height="35" src="https://tmssl.akamaized.net//images/beliebtheit/versus.png" width="39"/>
            <a class="fav-voting__link-player fav-voting__link-player--black" href="/beliebtheit/speichernSpieler?spieler_id_gewinner=344695&amp;spieler_id_verlierer=58358&amp;kontinent=0&amp;land=0&amp;wettbewerb=L1&amp;verein=27&amp;position=0&amp;marktwert=0&amp;spieler_id_1=58358&amp;lieblingsverein=0">
            <img alt="Dayot Upamecano" class="lazy" data-src="https://img.a.transfermarkt.technology/portrait/medium/344695-1667829882.jpg?lm=1" src="data:image/gif;base64,R0lGODlhAQABAIAAAMLCwgAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" title="Dayot Upamecano - source: IMAGO"/> <div class="fav-voting__name">
                                    Dayot Upamecano                    </div>
            <div class="fav-voting__club fav-voting__club--right">
            <img alt="Bayern Munich" class="" src="https://tmssl.akamaized.net/images/wappen/kaderquad/27.png?lm=1498251238" title="Bayern Munich"/> </div>
            </a>
            </div>
            </div>
            </section>
            <div class="werbung werbung-rectangle2"><!-- /22272936144,58778164/display_thirdparty/transfermarkt_uk/ros/bottom_mpu -->
            <div id="div-gpt-ad-bottom_mpu" style="width: 300px; height: 250px;"></div>
            <!-- End AdSlot 4 --></div> </div>
            </div>
            <div class="werbung werbung-fullsize_contentad"><!-- /22272936144,58778164/display_thirdparty/transfermarkt_uk/ros/bottom_banner -->
            <div id="div-gpt-ad-bottom_banner" style="min-width: 728px; min-height: 90px;"></div>
            <!-- End AdSlot 7 --></div> </main>
            <footer>
            <tm-language-hint></tm-language-hint>
            <div class="tm-footer">
            <a class="tm-footer__logo" href="/">
            <img alt="Transfermarkt" height="33" src="https://tmsi.akamaized.net/head/transfermarkt_logo.svg" width="80"/>
            </a>
            <ul class="tm-footer__links">
            <li class="tm-footer__links-item">
            <a href="/intern/impressum">
                    Legal notice      </a>
            </li>
            <li class="tm-footer__links-item">
            <a href="/intern/web/datenschutz">
                    Data protection      </a>
            </li>
            <li class="tm-footer__links-item">
            <a class="cmp-link" href="javascript:void(0)">
                    Privacy      </a>
            </li>
            <li class="tm-footer__links-item">
            <a href="/intern/anb">
                    General terms of use      </a>
            </li>
            <li class="tm-footer__links-item">
            <a href="/intern/tmteam">
                    The TM team      </a>
            </li>
            <li class="tm-footer__links-item">
            <a href="/intern/faq">
                    FAQ      </a>
            </li>
            <li class="tm-footer__links-item">
            <a href="/intern/fehlermelden">
                    Found a mistake?      </a>
            </li>
            </ul>
            </div>
            </footer>
            <div id="menue_overlay"></div>
            </div>
            <script type="text/javascript">
                            var iam_data = {
            "st":"transfer",
            "cp":"ausland_co.uk_r",
            "co":""
            }
                        </script>
            <script type="module">
                            var defaultOptions={tracking:!0,refreshAds:!0};export var refreshAd=function(){var e,n;[ASCDP.hasOwnProperty("adS"),null===(e=ASCDP.adS)||void 0===e?void 0:e.hasOwnProperty("reloadAds"),"function"==typeof(null===(n=ASCDP.adS)||void 0===n?void 0:n.reloadAds)].every(function(e){return e})&&ASCDP.adS.reloadAds()};export var TmTrackingAndAds=function(e,n){void 0===n&&(n=defaultOptions);var r=["tabelle","reiter","forum"].includes(e)?e:"";n.tracking&&(gtag("event","page_view",{page_path:"/jsContent"+window.location.pathname}),sendIvwData(r)),n.refreshAds&&"undefined"!=typeof ASCDP&&refreshAd()};window.tmTrackingAndAds=function(e,n){return TmTrackingAndAds(e,n)};
                        </script>
            <script type="text/javascript">
                            if(typeof IOMm === 'function') {
                                IOMm('configure', { st: iam_data.st, dn: 'data-84a0f3455d.transfermarkt.co.uk', mh:5 });
                                IOMm('pageview', { cp: iam_data.cp, co: iam_data.co });
                            } else {
                                console.warn('IOMm is not defined');
                            }
                        </script>
            <script type="text/javascript">
                    if(typeof(adet) == "boolean" && adet == false){
                            img_src="/static/singlepictures/jk99hhfsdh209nbnkjldgh90sghfsdlk";
                    } else {
                            img_src="/static/singlepictures/jku90whjlkjbwbta1g4b8h89fh8sgh8d";
                    }
                    var elem = document.createElement("img");
                    document.body.appendChild(elem);
                    elem.src = img_src;
            </script>
            <!-- Adition -->
            <div id="oddsServe">
            </div>
            <div id="werbung_recommender_sidebar_wrapper" style="display: none;">
            <div class="box" id="recommender_sidebar">
            <div class="OUTBRAIN" data-ob-template="DE_Transfermarkt.uk" data-src="https://www.transfermarkt.co.uk/thomas-muller/profil/spieler/58358" data-widget-id="SB_1"></div>
            </div>
            </div>
            </body>
            </html>
        """
    soup = BeautifulSoup(html_code, "html.parser")
    return soup


@pytest.fixture
def user_submission(
    user_submission_factory,
    football_player_factory,
    club_team_factory,
    national_team_factory,
):
    user_submission = user_submission_factory()
    bayern = club_team_factory(name="Bayern Munich")
    barca = club_team_factory(name="FC Barcelona")
    return user_submission
