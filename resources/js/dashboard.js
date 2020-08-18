const QuickSightEmbedding = require('amazon-quicksight-embedding-sdk');
window.$ = window.jQuery = require('jquery');
window.Popper = require('popper.js/dist/umd/popper.js').default;

require('bootstrap');

window.Dashboard = {};

function onDashboardLoad(payload) {
    console.log("Do something when the dashboard is fully loaded.");
}

function onError(payload) {
    console.log("Do something when the dashboard fails loading");
}

window.embedDashboard = function (url) {
    const containerDiv = document.getElementById("embeddingContainer");
    const options = {
        url,
        container: containerDiv,
        parameters: {},
        scrolling: "yes",
        locale: "pt-BR",
        footerPaddingEnabled: false
    };
    window.Dashboard = QuickSightEmbedding.embedDashboard(options);
    window.Dashboard.on("error", onError);
    window.Dashboard.on("load", onDashboardLoad);
}