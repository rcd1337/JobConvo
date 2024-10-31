import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';
import { SALARY_RANGE_EXPECTATION, EDUCATIONAL_LEVEL } from '../constants'; // Adjust the import path as necessary

const JobListingsEdit = () => {
    const { id } = useParams(); // Get the job listing ID from the URL
    const [jobDetail, setJobDetail] = useState({
        title: '',
        requirements: '',
        min_educational_level: '',
        salary_range: ''
    });
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const token = localStorage.getItem('token');
    const navigate = useNavigate(); // Hook to navigate programmatically

    useEffect(() => {
        const fetchJobDetail = async () => {
            try {
                const response = await axios.get(`http://localhost:8000/api/v1/job-listings/${id}/`, {
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                });
                setJobDetail(response.data);
            } catch (err) {
                setError('Failed to fetch job detail');
                alert(err.response?.data?.detail || 'Failed to fetch job detail');
            } finally {
                setLoading(false);
            }
        };

        fetchJobDetail();
    }, [id, token]);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setJobDetail({ ...jobDetail, [name]: value });
    };

    const handleUpdate = async () => {
        const { id, recruiter, ...updateData } = jobDetail;
    
        try {
            await axios.patch(`http://localhost:8000/api/v1/job-listings/${id}/`, updateData, {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });
            alert('Job listing updated successfully!');
            navigate(`/job-listings/${id}`); // Redirect to the job listing detail page after updating
        } catch (err) {
            console.error('Error updating job listing:', err); // Log the error for more insight
            alert(err.response?.data?.detail || 'Failed to update job listing');
        }
    };
    

    if (loading) {
        return <div style={{ textAlign: 'center', marginTop: '50px' }}>Loading...</div>;
    }

    if (error) {
        return <div style={{ textAlign: 'center', marginTop: '50px' }}>{error}</div>;
    }

    return (
        <div style={{ textAlign: 'left', margin: '50px auto', maxWidth: '600px' }}>
            <h2 style={{ textAlign: 'center' }}>Edit Job Listing</h2>

            <div>
                <label>
                    Title:
                    <input
                        type="text"
                        name="title"
                        value={jobDetail.title}
                        onChange={handleChange}
                        style={{ width: '100%', margin: '10px 0' }}
                    />
                </label>

                <label>
                    Requirements:
                    <textarea
                        name="requirements"
                        value={jobDetail.requirements}
                        onChange={handleChange}
                        style={{ width: '100%', margin: '10px 0' }}
                    />
                </label>

                <label>
                    Minimum Educational Level:
                    <select
                        name="min_educational_level"
                        value={jobDetail.min_educational_level}
                        onChange={handleChange}
                        style={{ width: '100%', margin: '10px 0' }}
                    >
                        <option value="" disabled>Select Educational Level</option>
                        {Object.values(EDUCATIONAL_LEVEL).map((level) => (
                            <option key={level.value} value={level.value}>
                                {level.label}
                            </option>
                        ))}
                    </select>
                </label>

                <label>
                    Salary Range:
                    <select
                        name="salary_range"
                        value={jobDetail.salary_range}
                        onChange={handleChange}
                        style={{ width: '100%', margin: '10px 0' }}
                    >
                        <option value="" disabled>Select Salary Range</option>
                        {Object.values(SALARY_RANGE_EXPECTATION).map((range) => (
                            <option key={range.value} value={range.value}>
                                {range.label}
                            </option>
                        ))}
                    </select>
                </label>
            </div>

            <div style={{ marginTop: '20px', textAlign: 'center' }}>
                <button onClick={() => navigate(-1)} style={{ margin: '5px', padding: '10px 15px' }}>Cancel</button>
                <button onClick={handleUpdate} style={{ margin: '5px', padding: '10px 15px' }}>Confirm</button>
            </div>
        </div>
    );
};

export default JobListingsEdit;
