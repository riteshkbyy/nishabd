// Set Pagination Link Variable
var linkHeader = "";

// Handle a Simple AJAX Get Request
function ajaxGet(url) {
    return new Promise(function(resolve, reject) {
        var request = new XMLHttpRequest();
        request.open("GET", url);
        request.onload = function() {
            if (request.status === 200) {
                resolve(request.response);
linkHeader = request.getResponseHeader("Link");
            } else {
                reject(new Error(request.statusText));
            }
        };

        request.onerror = function() {
            reject(new Error("Network Error"));
        };

        request.send();
    });
}

// Render Articles List on the Page
function renderArticles(articles) {
var output = "";

if (linkHeader != undefined) {
var links = parseLinkHeader(linkHeader);
renderPagination(links);
}

// TODO: Cleanup this output code.
for(var article = 0; article < articles.length; article++) {
output += "<div  class='masonry  hoverable col l4 m6 s12 z-index-0' id='linking'><div class='panel'><a href='" +
articles[article].url +
"' target='_blank' class='panel-body card-title'><h5 class='mv-lg text-bold'>" +
articles[article].title +
"</h5></a><div class='divider'></div><a href='" +
articles[article].url +
"' target='_blank' class='panel-body black-text bold-text card-content center '><p id='description-wrapper'>" +
articles[article].description +
"</p><p class='clearfix'><span class='clearfix left'><small class='mr-sm'>" +
articles[article].publication_date +
"</small></span><span class='pull-right'><div class='card-action'><a class='right red-text z-index-0' href='" +
articles[article].url +
"' target='_blank' title='Read More'>Read More</a></div></span></p></div></a></div>";
}

document.getElementById("loading-wrapper").style.display = "none";
document.getElementById("articles-wrapper").innerHTML = output;
document.getElementById("pagination-wrapper").style.display = "block";
}

window.onload = function () {
var apiUrl = "/api" + window.location.pathname;
var loadingMessage = randomLoadingMessage();
var currentPage = getQueryString('page') || 1;
var daysFilter = getQueryString('days');



if (daysFilter != undefined) {
apiUrl += "?days=" + daysFilter + "&page=" + currentPage
} else {
apiUrl += "?page=" + currentPage
}

document.getElementById("loading-message").innerHTML = loadingMessage;

// Perform the AJAX Get Request
ajaxGet(apiUrl).then(JSON.parse).then(
function(objects) { return this.renderArticles(objects); }
).catch(function(error) { throw new ApplicationError(error); });
}

