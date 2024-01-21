function loadJSON(selector) {
    return JSON.parse(document.querySelector(selector).getAttribute('data-json'))
}

window.onload = function () {
  // gets a canvas element from index.html file
  const ctx = document.getElementById("pieChart");

  // Gets an element with id from index.html
  let jsonData = loadJSON("#jsonData");

  // Gathers and destructured data from db
  let labels = jsonData.map(({ category }) => category);
  let amount = jsonData.map(({ amount }) => amount);

  console.log('labels', jsonData.map(item => item))


  // creates charts on a canvas element
  new Chart(ctx, {
    type: "line",
    data: {
      datasets: [
        {
          data: amount,
          label: "Amount",
          // This binds the dataset to the left y-axis
          yAxisID: "left-y-axis",
        },
        {
          data: labels,
          label: "Category",
          // This binds the dataset to the right y-axis
          yAxisID: "right-y-axis",
        },
      ],
      // creates the labels on the x-axis
      labels,
    },
    // options to set with chart
    options: {
      scales: {
        // binds options to the id from above
        "left-y-axis": {
          type: "linear",
          position: "left",
          title: { display: true, text: "Mood" },
        },
        "right-y-axis": {
          type: "linear",
          position: "right",
          title: { display: true, text: "Sleep" },
        },
      },
    },
  });
};

// window.onload = function () {
//   let jsonData = loadJson('#jsonData');
//
//
//   let data = jsonData.map(({amount}) => amount);
//   let labels = jsonData.map(({category}) => category);
//
//   console.log(data);
//   console.log(labels);
//
//   let config = {
//     type: 'bar',
//     data: {
//       labels: labels,
//       datasets: [
//         {
//           label: 'A random dataset',
//           backgroundColor: 'black',
//           borderColor: 'lightblue',
//           data: data,
//           fill: false
//         }
//       ]
//     },
//     options: {
//       responsive: true
//     }
//   };
//
//   let ctx = document.getElementById('pieChart').getContext('2d');
//   new Chart(ctx, config);
// };