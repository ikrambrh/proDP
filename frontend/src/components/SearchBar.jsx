import React, { useState } from 'react';

const SearchBar = ({ onSearch }) => {
  const [searchTerm, setSearchTerm] = useState('');

  const handleSearch = (e) => {
    setSearchTerm(e.target.value);
    if (onSearch) {
      onSearch(e.target.value);
    }
  };

  return (
    <div style={{ margin: '20px 0' }}>
      <input
        type="text"
        value={searchTerm}
        onChange={handleSearch}
        placeholder="Rechercher..."
        style={{
          padding: '10px 15px',
          fontSize: '16px',
          width: '300px',
          borderRadius: '25px',
          border: '2px solid #1e90ff',
          outline: 'none',
          backgroundColor: '#f0f8ff',
          transition: 'all 0.3s ease',
        }}
        onFocus={(e) => e.target.style.boxShadow = '0 0 5px #1e90ff'}
        onBlur={(e) => e.target.style.boxShadow = 'none'}
      />
    </div>
  );
};

export default SearchBar; 