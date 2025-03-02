'use client';

import SearchBar from '../components/SearchBar';

export default function Home() {
  const handleSearch = (term) => {
    console.log('Recherche :', term);
  };

  return (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      padding: '20px',
      minHeight: '100vh'
    }}>
      <h1 style={{ marginBottom: '20px' }}>Ma Recherche</h1>
      <SearchBar onSearch={handleSearch} />
      <h2>Test 1-2</h2>
    </div>
  );
}