import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';

const JobListingsDetail = () => {
    const { id } = useParams(); // Get the job listing ID from the URL
    const [jobDetail, setJobDetail] = useState(null);
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

    const handleDelete = async () => {
        try {
            await axios.delete(`http://localhost:8000/api/v1/job-listings/${id}/`, {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });
            alert('Job listing deleted successfully!');
            navigate('/job-listings'); // Redirect to job listings page after deletion
        } catch (err) {
            alert(err.response?.data?.detail || 'Failed to delete job listing');
        }
    };

    const handleApply = async () => {
        try {
            await axios.post(`http://localhost:8000/api/v1/job-listings/${id}/apply_to_job/`, {}, {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });
            alert('Successfully applied for the job!');
            window.location.reload(); // Refresh the page after successful application
        } catch (err) {
            alert(err.response?.data?.detail || 'Failed to apply for the job');
        }
    };

    // New function to handle edit button click
    const handleEdit = () => {
        navigate(`/job-listings/${id}/edit`); // Redirect to the edit page
    };

    if (loading) {
        return <div style={{ textAlign: 'center', marginTop: '50px' }}>Loading...</div>;
    }

    if (error) {
        return <div style={{ textAlign: 'center', marginTop: '50px' }}>{error}</div>;
    }

    return (
        <div style={{ textAlign: 'left', margin: '50px auto', maxWidth: '600px' }}>
            <h2 style={{ textAlign: 'center' }}>{jobDetail.title}</h2>
            <p><strong>Requirements:</strong> {jobDetail.requirements}</p>
            <p><strong>Minimum Educational Level:</strong> {jobDetail.min_educational_level}</p>
            <p><strong>Recruiter ID:</strong> {jobDetail.recruiter}</p>
            
            {/* Move buttons above Applicants section */}
            <div style={{ marginTop: '20px', textAlign: 'center' }}>
                <button onClick={handleApply} style={{ margin: '5px', padding: '10px 15px' }}>Apply</button>
                <button onClick={handleDelete} style={{ margin: '5px', padding: '10px 15px' }}>Delete</button>
                <button onClick={handleEdit} style={{ margin: '5px', padding: '10px 15px' }}>Edit</button>
            </div>

            <h3>Applicants:</h3>
            <hr style={{ border: '1px solid #ccc' }} />
            {jobDetail.applicants.length > 0 ? (
                <ul style={{ listStyleType: 'none', padding: 0 }}>
                    {jobDetail.applicants.map((applicant, index) => (
                        <li key={applicant.id} style={{ marginBottom: '10px' }}>
                            <p><strong>Applicant ID:</strong> {applicant.applicant}</p>
                            <p><strong>Applicant Email:</strong> {applicant.applicant_email}</p>
                            <p><strong>Applicant Ranking:</strong> {applicant.applicant_ranking}</p>
                            <p><strong>Application Created At:</strong> {new Date(applicant.created_at).toLocaleString()}</p>
                            {index < jobDetail.applicants.length - 1 && (
                                <hr style={{ border: '1px solid #ccc' }} />
                            )}
                        </li>
                    ))}
                </ul>
            ) : (
                <p>No applicants yet</p>
            )}
        </div>
    );
};

export default JobListingsDetail;
