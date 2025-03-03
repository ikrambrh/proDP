'use client';

import Sidebar from '../components/Sidebar'; // Import your Sidebar component
import SearchBar from '../components/SearchBar';

export default function Home() {
  const handleSearch = (term) => {
    console.log('Recherche :', term);
  };

  return (
    <div className="flex min-h-screen">
      {/* Sidebar on the left */}
      <Sidebar />

      {/* Main content area */}
      <div className="flex-1 p-6 bg-gray-100">
        <h1 className="text-2xl font-bold mb-4">Ma Recherche</h1>
        <SearchBar onSearch={handleSearch} />
        <h2 className="mt-4">Test 1-2</h2>
      </div>
    </div>
  );
}
