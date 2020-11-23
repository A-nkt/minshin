var ctx3 = document.getElementById("myPieChart3");
var myPieChart3 = new Chart(ctx3, {
  type: 'pie',
  data: {
    labels: ["500~600点", "600~700点", "700~800点", "800~900点","900点以上"],
    datasets: [{
        backgroundColor: [
            "#BB5179",
            "#FAFF67",
            "#58A27C",
            "#3C00FF",
            "black",
        ],
        data: [4,3,2,3,1]
    }]
  },
  options: {
    tooltips: {
      titleFontSize: 24,
      bodyFontSize: 24,
    },
    title: {
      display: true,
      text: '理学系研究科 点数割合',
      fontSize: 28,
    },
    legend: {
          labels: {
              fontSize: 24,
          }
      },
  }
});
