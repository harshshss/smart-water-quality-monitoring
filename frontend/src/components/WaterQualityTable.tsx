import React from 'react';
import { WaterQualityData } from '../types/WaterQuality';
import './WaterQualityTable.css';

interface WaterQualityTableProps {
  data: WaterQualityData;
}

const WaterQualityTable: React.FC<WaterQualityTableProps> = ({ data }) => {
  const getStatusClass = (status: string) => {
    switch (status.toLowerCase()) {
      case 'excellent':
        return 'status-excellent';
      case 'good':
        return 'status-good';
      case 'fair':
        return 'status-fair';
      case 'poor':
        return 'status-poor';
      default:
        return 'status-unknown';
    }
  };

  return (
    <div className="water-quality-table-container">
      <h2 className="table-title">Water Quality Data for {data.area}</h2>
      <table className="water-quality-table">
        <thead>
          <tr>
            <th>Parameter</th>
            <th>Value</th>
            <th>Unit</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td className="parameter-name">Turbidity</td>
            <td className="parameter-value">{data.turbidity}</td>
            <td className="parameter-unit">NTU</td>
            <td className={`parameter-status ${getStatusClass(data.status)}`}>
              {data.status}
            </td>
          </tr>
          <tr>
            <td className="parameter-name">pH Level</td>
            <td className="parameter-value">{data.ph}</td>
            <td className="parameter-unit">pH</td>
            <td className={`parameter-status ${getStatusClass(data.status)}`}>
              {data.status}
            </td>
          </tr>
          <tr>
            <td className="parameter-name">Total Dissolved Solids (TDS)</td>
            <td className="parameter-value">{data.tds}</td>
            <td className="parameter-unit">ppm</td>
            <td className={`parameter-status ${getStatusClass(data.status)}`}>
              {data.status}
            </td>
          </tr>
          <tr className="overall-status-row">
            <td className="parameter-name overall-label">Overall Status</td>
            <td className="parameter-value">-</td>
            <td className="parameter-unit">-</td>
            <td className={`parameter-status overall-status ${getStatusClass(data.status)}`}>
              {data.status}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default WaterQualityTable;
