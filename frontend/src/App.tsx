import React, { useState, useEffect } from 'react';
import './App.css';
import Header from './components/Header';
import AreaSelector from './components/AreaSelector';
import WaterQualityTable from './components/WaterQualityTable';
import Footer from './components/Footer';
import { WaterQualityData } from './types/WaterQuality';

const App: React.FC = () => {
  const [areas, setAreas] = useState<string[]>([]);
  const [selectedArea, setSelectedArea] = useState<string>('');
  const [waterQualityData, setWaterQualityData] = useState<WaterQualityData | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string>('');

  const API_BASE_URL = 'http://localhost:5000/api';

  // Fetch available areas on component mount
  useEffect(() => {
    fetchAreas();
  }, []);

  // Fetch water quality data when area is selected
  useEffect(() => {
    if (selectedArea) {
      fetchWaterQualityData(selectedArea);
    }
  }, [selectedArea]);

  const fetchAreas = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/areas`);
      const data = await response.json();
      setAreas(data.areas);
      if (data.areas.length > 0) {
        setSelectedArea(data.areas[0]); // Select first area by default
      }
    } catch (err) {
      setError('Failed to fetch areas');
      console.error('Error fetching areas:', err);
    }
  };

  const fetchWaterQualityData = async (area: string) => {
    setLoading(true);
    setError('');
    try {
      const response = await fetch(`${API_BASE_URL}/water-quality/${area}`);
      if (!response.ok) {
        throw new Error('Area not found');
      }
      const data = await response.json();
      setWaterQualityData(data);
    } catch (err) {
      setError('Failed to fetch water quality data');
      setWaterQualityData(null);
      console.error('Error fetching water quality data:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleAreaChange = (area: string) => {
    setSelectedArea(area);
  };

  return (
    <div className="App">
      <Header />
      <main className="main-content">
        <div className="container">
          <AreaSelector 
            areas={areas}
            selectedArea={selectedArea}
            onAreaChange={handleAreaChange}
          />
          
          {error && (
            <div className="error-message">
              {error}
            </div>
          )}
          
          {loading ? (
            <div className="loading">Loading water quality data...</div>
          ) : (
            waterQualityData && (
              <WaterQualityTable data={waterQualityData} />
            )
          )}
        </div>
      </main>
      <Footer />
    </div>
  );
};

export default App;
