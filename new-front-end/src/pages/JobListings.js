import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom'; // Import Link for navigation

const JobListings = () => {
    const [jobListings, setJobListings] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const token = localStorage.getItem('token');

    useEffect(() => {
        const fetchJobListings = async () => {
            try {
                const response = await axios.get('http://localhost:8000/api/v1/job-listings/', {
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                });
                setJobListings(response.data.results);
            } catch (err) {
                setError('Failed to fetch job listings');
                alert(err.response?.data?.detail || 'Failed to fetch job listings');
            } finally {
                setLoading(false);
            }
        };

        fetchJobListings();
    }, [token]);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>{error}</div>;
    }

    return (
        <div style={{ textAlign: 'center', marginTop: '50px' }}>
            <h2>Job Listings</h2>
            <ul style={{ listStyleType: 'none', padding: 0 }}>
                {jobListings.map((job) => (
                    <li key={job.id} style={{ border: '1px solid #ccc', margin: '10px', padding: '10px' }}>
                        <Link to={`/job-listings/${job.id}`} style={{ textDecoration: 'none', color: 'black' }}>
                            <h3 style={{ textDecoration: 'underline', color: 'blue' }}>{job.title}</h3>
                        </Link>
                        <p><strong>Requirements:</strong> {job.requirements}</p>
                        <p><strong>Minimum Educational Level:</strong> {job.min_educational_level}</p>
                        <p><strong>Salary Range:</strong> {job.salary_range}</p>
                        <p><strong>Created At:</strong> {new Date(job.created_at).toLocaleString()}</p>
                        <p><strong>Updated At:</strong> {new Date(job.updated_at).toLocaleString()}</p>
                        <p><strong>Number of Applicants:</strong> {job.number_of_applicants}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default JobListings;
