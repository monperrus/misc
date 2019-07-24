// ==UserScript==
// @name          direct-bibtex-in-google-scholar
// @description   add a bibtex link in Google Scholar (direct-bibtex-in-google-scholar)
// @url           http://www.monperrus.net/martin/direct-bibtex-in-google-scholar
// @namespace     http://www.monperrus.net/martin/
// @author        Martin Monperrus <martin.monperrus@gnieh.org>
// @author        Nicolas Harrand <Nicolas Harrand <harrand@kth.se>>
// @license       MIT
// @version       0.2
// @include       *://scholar.google.tld/*
// @require       https://ajax.googleapis.com/ajax/libs/jquery/1.5.1/jquery.min.js
// @grant         GM_xmlhttpRequest
// @grant         GM_setClipboard
// ==/UserScript==


var $ = window.jQuery;
function main() {
    // for each result of google scholar
    $(".gs_r").each(
        function (index, result) {
            // getting the paper title
            var text = $(result).find('.gs_rt').text();

            // where to add the data: add the end of the menu which is under each entry
            var whereList = $(result).find('.gs_fl')
            var where = $(whereList.get(whereList.length - 1));

            // we create a DIV object to contain the bibtex data
            var container = $('<pre/>');
            where.after(container);

            // adding a link to trigger the bibtex download
            var noteLink = $('<a href="javascript:void(0)">&nbsp;&nbsp;Bibtex</a>');
            noteLink.click(function() {
               var elem = $(result).find('a.gs_nph').get(1); // .contains('Cite')
              	//console.log("test: " + $(result).attr('data-cid'));

                // the identifier is in a JS function gs_cite(0,'ID',1)
                // we parse it with a regex
          			//console.log("pre: " + $(elem).attr("onclick").toString());
                //var gsid = $(elem).attr("onclick").toString().match(/,'(.*)','/)[1];
                var gsid = $(result).attr('data-cid');
          		//console.log("gsid: " + gsid);

                // we build a first URL
                var url1 = "scholar?q=info:"+gsid+":scholar.google.com/&output=cite";
          		//console.log("url1: " + url1);

                // calling it with AJAX
                $.ajax({"url" : url1,
                       success: function(data) {
                           // the final url, hosted on googleusercontent.com
                           // so there is a need for a cross-domain call
                           var url2 = ($(data).find('.gs_citi').attr('href'));
                           //console.log("url2: " + url2);
                           GM_xmlhttpRequest({
                                method:     'GET',
                                url:        url2,
                                onload:     function (responseDetails) {
                                                container.text("%% also copied to clipboard \n"+responseDetails.responseText);
                                                GM_setClipboard(responseDetails.responseText);
                                            }
                            });
                       }
               });
            });
            var noteEnvelop = $('<span> - </span>');
            noteEnvelop.append(noteLink);
            where.append(noteEnvelop);
        });
}


main();
