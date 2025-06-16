const renderCombinedChart = (incomeData, expenseData, incomeLabels, expenseLabels) => {
    const ctx = document.getElementById('expenseChart').getContext('2d');

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: [...incomeLabels, ...expenseLabels],
            datasets: [{
                label: 'Incomes',
                data: [...incomeData, ...Array(expenseData.length).fill(0)],
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }, {
                label: 'Expenses',
                data: [...Array(incomeData.length).fill(0), ...expenseData],
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top',
                },
                tooltip: {
                    enabled: true
                },
                title: {
                    display: true,
                    text: 'Incomes and Expenses Comparison',
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
};

const getChartData = () => {
    console.log('Fetching income and expense data...');
    Promise.all([
        fetch('income_source_summary').then(res => res.json()),
        fetch('/expense_category_summary').then(res => res.json())
    ]).then(([incomeResults, expenseResults]) => {
        console.log("Income results", incomeResults);
        console.log("Expense results", expenseResults);

        const incomeData = Object.values(incomeResults.income_source_data);
        const incomeLabels = Object.keys(incomeResults.income_source_data);

        const expenseData = Object.values(expenseResults.expense_category_data);
        const expenseLabels = Object.keys(expenseResults.expense_category_data);

        renderCombinedChart(incomeData, expenseData, incomeLabels, expenseLabels);
    }).catch(error => {
        console.error('Error fetching data:', error);
    });
};

document.addEventListener('DOMContentLoaded', getChartData);