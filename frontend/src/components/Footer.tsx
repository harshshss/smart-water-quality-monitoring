import React from 'react';
import './Footer.css';

const Footer: React.FC = () => {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="app-footer">
      <div className="container">
        <p className="footer-text">
          © {currentYear} Smart Water Quality Monitoring. All rights reserved.
        </p>
        <p className="footer-subtitle">
          Monitoring water quality across Northeast India
        </p>
      </div>
    </footer>
  );
};

export default Footer;
