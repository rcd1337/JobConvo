import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { SALARY_RANGE_EXPECTATION, EDUCATIONAL_LEVEL } from '../constants'; // Adjust the import path as necessary

const JobListingCreate = () => {
    const [jobDetail, setJobDetail] = useState({
        title: '',
        requirements: '',
        min_educational_level: '',
        salary_range: ''
    });
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const token = localStorage.getItem('token');
    const navigate = useNavigate(); // Hook to navigate programmatically

    const handleChange = (e) => {
        const { name, value } = e.target;
        setJobDetail({ ...jobDetail, [name]: value });
    };

    const handleCreate = async () => {
        console.log('Creating job listing with data:', jobDetail); // Log the data being sent
        setLoading(true); // Start loading state
        try {
            const response = await axios.post(`http://localhost:8000/api/v1/job-listings/`, jobDetail, {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });
            alert('Job listing created successfully!');
            const createdJobId = response.data.id; // Get the ID of the created job listing
            navigate(`/job-listings/${createdJobId}`); // Redirect to the newly created job listing page
        } catch (err) {
            console.error('Error creating job listing:', err); // Log the error for more insight
            alert(err.response?.data?.detail || 'Failed to create job listing');
        } finally {
            setLoading(false); // Stop loading state
        }
    };

    return (
        <div style={{ textAlign: 'left', margin: '50px auto', maxWidth: '600px' }}>
            <h2 style={{ textAlign: 'center' }}>Create Job Listing</h2>

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
                <button onClick={handleCreate} style={{ margin: '5px', padding: '10px 15px' }} disabled={loading}>
                    {loading ? 'Creating...' : 'Create'}
                </button>
            </div>
        </div>
    );
};

export default JobListingCreate;
