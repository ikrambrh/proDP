"use client";
import Sidebar from "@/components/Sidebar";
import TopBar from "@/components/TopBar";

export default function traitements() {
    return (
        <div className="flex min-h-screen">
        {/* Sidebar (Fixed Position) */}
        <Sidebar />
  
        {/* Main Content (Add margin to prevent overlap) */}
        <div className="flex-1 flex flex-col ml-64">  
          {/* Top Navigation Bar */}
          <TopBar />
  
          {/* Main Page Content */}
          <div className="p-6">
            {/* Your page content goes here */}
            <h1 className="text-2xl font-bold">Page traitements</h1>
          </div>
        </div>
      </div>
    );
  }