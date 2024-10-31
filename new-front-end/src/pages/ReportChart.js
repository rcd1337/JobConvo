import React, { useEffect, useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, CartesianGrid } from 'recharts';
import '../App.css';

const ReportChart = ({ year, month, data }) => {
    const [chartData, setChartData] = useState([]);
    const [errorMessage, setErrorMessage] = useState('');

    useEffect(() => {
        if (data && data.length > 0) {
            setChartData(data); // Use the total data directly if provided
        } else {
            // Fetch data if year or month is provided
            const fetchData = async () => {
                try {
                    const token = localStorage.getItem('token');
                    const url = new URL('http://localhost:8000/api/v1/report/');

                    if (year) url.searchParams.append('year', year);
                    if (month) url.searchParams.append('month', month);

                    const response = await fetch(url, {
                        method: 'GET',
                        headers: {
                            'Authorization': `Bearer ${token}`,
                            'Content-Type': 'application/json',
                        },
                    });

                    if (!response.ok) {
                        throw new Error(response.statusText);
                    }

                    const result = await response.json();

                    setChartData([
                        { name: 'Vagas Criadas', count: result.job_listings_amount },
                        { name: 'Candidatos Recebidos', count: result.applications_amount },
                    ]);
                } catch (error) {
                    setErrorMessage(`Error fetching data: ${error.message}`);
                }
            };

            if (year || month) {
                fetchData();
            }
        }
    }, [year, month, data]);

    return (
        <div className="chart-container">
            {errorMessage && <div className="error-alert">{errorMessage}</div>}
            {chartData.length > 0 && (
                <BarChart width={600} height={300} data={chartData}>
                    <XAxis dataKey="name" />
                    <YAxis />
                    <Tooltip />
                    <Legend />
                    <CartesianGrid strokeDasharray="3 3" />
                    <Bar dataKey="count" fill="#8884d8" />
                </BarChart>
            )}
        </div>
    );
};

export default ReportChart;
