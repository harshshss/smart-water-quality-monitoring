import React from 'react';
import './Header.css';

const Header: React.FC = () => {
  return (
    <header className="app-header">
      <div className="container">
        <h1 className="app-title">Smart Water Quality Monitoring</h1>
        <p className="app-subtitle">Northeast India Water Quality Data</p>
      </div>
    </header>
  );
};

export default Header;
