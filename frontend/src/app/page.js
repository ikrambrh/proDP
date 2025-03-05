'use client';

import Sidebar from '../components/Sidebar'; // Sidebar on the left
import TopBar from '../components/TopBar'; // Top navigation bar

export default function Home() {

  return (
    <div className="flex min-h-screen">
      {/* Sidebar on the left */}
      <Sidebar />

      {/* Main content area */}
      <div className="flex-1 flex flex-col">
        {/* TopBar at the top */}
        <TopBar />

      
      </div>
    </div>
  );
}
