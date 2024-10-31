import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MainPage from './pages/MainPage';
import SignIn from './pages/SignIn';
import UnifiedSignUp from './pages/UnifiedSignUp';
import JobListings from './pages/JobListings';
import JobListingsDetail from './pages/JobListingsDetail';
import JobListingsEdit from './pages/JobListingsEdit';
import JobListingsCreate from './pages/JobListingsCreate';
import Report from './pages/Report';
import Navbar from './Navbar';

const App = () => {
    return (
        <Router>
          <Navbar />
          <Routes>
              <Route path="/" element={<MainPage />} />
              <Route path="/signin" element={<SignIn />} />
              <Route path="/signup" element={<UnifiedSignUp />} />
              <Route path="/job-listings" element={<JobListings />} />
              <Route path="/job-listings/:id" element={<JobListingsDetail />} />
              <Route path="/job-listings/:id/edit" element={<JobListingsEdit />} />
              <Route path="/job-listings/create" element={<JobListingsCreate />} />
              <Route path="/report" element={<Report />} />
          </Routes>
        </Router>
    );
};

export default App;
