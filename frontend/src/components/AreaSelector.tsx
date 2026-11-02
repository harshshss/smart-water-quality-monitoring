import React from 'react';
import './AreaSelector.css';

interface AreaSelectorProps {
  areas: string[];
  selectedArea: string;
  onAreaChange: (area: string) => void;
}

const AreaSelector: React.FC<AreaSelectorProps> = ({ areas, selectedArea, onAreaChange }) => {
  const handleChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    onAreaChange(event.target.value);
  };

  return (
    <div className="area-selector">
      <label htmlFor="area-select" className="area-selector-label">
        Select Area:
      </label>
      <select
        id="area-select"
        className="area-selector-dropdown"
        value={selectedArea}
        onChange={handleChange}
      >
        <option value="" disabled>
          Choose an area
        </option>
        {areas.map((area) => (
          <option key={area} value={area}>
            {area}
          </option>
        ))}
      </select>
    </div>
  );
};

export default AreaSelector;
