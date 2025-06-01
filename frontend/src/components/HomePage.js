import React, { useEffect, useState } from 'react';

const HomePage = () => {
  const [status, setStatus] = useState('');

  useEffect(() => {
    const fetchStatus = async () => {
      try {
        const backendUrl = process.env.REACT_APP_BACKEND_URL || import.meta.env.REACT_APP_BACKEND_URL;
        const response = await fetch(`${backendUrl}/api/`);
        const data = await response.json();
        setStatus(data.message);
      } catch (error) {
        console.error('Error fetching status:', error);
        setStatus('Error connecting to backend');
      }
    };

    fetchStatus();
  }, []);

  return (
    <div className="homepage">
      <div className="hero-section">
        <div className="hero-content">
          <img 
            src="https://images.unsplash.com/photo-1488590528505-98d2b5aba04b?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" 
            alt="Hub Editor" 
            className="hero-image"
          />
          <h1 className="hero-title">Building something incredible ~!</h1>
          <p className="hero-subtitle">Welcome to Hub Editor - Your gateway to innovation and insights</p>
          {status && <p className="status-text">Status: {status}</p>}
        </div>
      </div>
    </div>
  );
};

export default HomePage;