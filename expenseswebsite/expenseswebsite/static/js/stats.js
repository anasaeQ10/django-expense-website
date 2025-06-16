const renderChart=(data,labels)=>{
    const ctx = document.getElementById('myChart').getContext('2d');

new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: labels,
        datasets: [{
            label: 'last 6 months expenses',
            data: data,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        cutout: '70%',
        plugins: {
            legend: {
                position: 'top',
            },
            tooltip: {
                enabled: true
            },
            title: {
                display: true,
                text: 'Expenses per Category',
                font: {
                    size: 18,
                    family: 'Arial',
                    weight: 'bold',
                },
                padding: {
                    top: 10,
                    bottom: 30
                }
            }
        }
    }
});
}

const getChartData=()=>{
    console.log('fitching');
    fetch('/expense_category_summary')
    .then((res) => res.json())
    .then((results) => {
        console.log("results",results);
        const category_data=results.expense_category_data;
        //const labels = data.map(item=>item.category_name);
        const [labels, data]=[Object.keys(category_data),Object.values(category_data),];
        renderChart(data,labels);
    });
};

document.onload=getChartData();


