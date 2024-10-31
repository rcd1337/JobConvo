import React, { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import ReportChart from './ReportChart';

const Report = () => {
    const { search } = useLocation();
    const navigate = useNavigate(); // To change the URL
    const query = new URLSearchParams(search);
    const year = query.get('year');
    const month = query.get('month');

    const [totalData, setTotalData] = useState([]);
    const [isLoading, setIsLoading] = useState(true);
    const [errorMessage, setErrorMessage] = useState('');
    const [inputYear, setInputYear] = useState(new Date().getFullYear()); // Start from the current year
    const [inputMonth, setInputMonth] = useState('');

    useEffect(() => {
        const fetchTotalData = async () => {
            try {
                const token = localStorage.getItem('token');
                const response = await fetch('http://localhost:8000/api/v1/report/', {
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
                setTotalData([
                    { name: 'Vagas Criadas', count: result.job_listings_amount },
                    { name: 'Candidatos Recebidos', count: result.applications_amount },
                ]);
            } catch (error) {
                setErrorMessage(`Error fetching total data: ${error.message}`);
            } finally {
                setIsLoading(false);
            }
        };

        // Fetch total data if no year and month are provided
        if (!year && !month) {
            fetchTotalData();
        }
    }, [year, month]);

    const handleFilter = () => {
        // Update the URL with the year and month
        navigate(`/report?year=${inputYear}&month=${inputMonth}`);
    };

    // Function to check if both inputs have values
    const isFilterButtonEnabled = () => {
        return String(inputYear).trim() !== '' && String(inputMonth).trim() !== '';
    };

    return (
        <div style={{ textAlign: 'center', margin: '20px' }}>
            <h1>Report</h1>
            {year && month ? (
                <ReportChart year={year} month={month} />
            ) : (
                <div>
                    <h2>(Total)</h2>
                    {isLoading ? (
                        <p>Loading...</p>
                    ) : errorMessage ? (
                        <div className="error-alert">{errorMessage}</div>
                    ) : (
                        <ReportChart data={totalData} /> // Pass the total data directly
                    )}
                </div>
            )}
            <div style={{ marginTop: '20px' }}>
                <input
                    type="number"
                    placeholder="Year"
                    value={inputYear}
                    onChange={(e) => setInputYear(e.target.value)}
                    style={{ width: '100px', marginRight: '10px' }} // Set width and margin
                />
                <input
                    type="number"
                    placeholder="Month"
                    value={inputMonth}
                    onChange={(e) => setInputMonth(e.target.value)}
                    min="1"
                    max="12"
                    style={{ width: '100px', marginRight: '10px' }} // Set width and margin
                />
                <button onClick={handleFilter} disabled={!isFilterButtonEnabled()}>Filter</button>
            </div>
        </div>
    );
};

export default Report;
