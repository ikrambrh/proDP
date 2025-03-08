"use client";

import { useState } from "react";
import Sidebar from "@/components/Sidebar";
import TopBar from "@/components/TopBar";
import Tabs from "@/components/Tabs";
import { Plus, Save, FileUp, ChevronDown } from "lucide-react"; // Import Lucide icons

export default function ConsentementsPage() {
  const [activeTab, setActiveTab] = useState({
    mainTab: "notices",
    subTab: "creation",
  });

  const [category, setCategory] = useState("Client");
  const [date, setDate] = useState("");
  const [version, setVersion] = useState("1.0.0");

  const tabsConfig = [
    {
      key: "notices",
      label: "Notices d'information et de consentement",
      subTabs: [
        { key: "creation", label: "Création" },
        { key: "diffusion", label: "Diffusion" },
        { key: "archivage", label: "Archivage" },
      ],
    },
    {
      key: "gestion",
      label: "Gestion et suivi des consentements",
    },
  ];

  return (
    <div className="flex">
      {/* Sidebar */}
      <Sidebar />

      {/* Main Content */}
      <div className="flex-1 flex flex-col ml-64 bg-gray-100">
        {/* Top Bar */}
        <TopBar />

        {/* Title & Buttons */}
        <div className="flex justify-between items-center px-6 py-4 bg-gray-100 shadow-md">
          <h1 className="text-xl font-bold text-gray-800">
            Gestion des consentements
          </h1>
          <button className="flex items-center bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">
            <Plus className="mr-2" size={18} /> Créer un template
          </button>
        </div>

        {/* Tabs Component */}
        <Tabs tabs={tabsConfig} onTabChange={setActiveTab} />

        {/* Page Content */}
        <div className="p-6">
          {/* Section: Selection Inputs */}
          {activeTab.mainTab === "notices" && activeTab.subTab === "creation" && (
            <div className="bg-white p-6 mt-4 shadow-md rounded-lg">
              <div className="grid grid-cols-3 gap-4">
                {/* Category Dropdown */}
                <div>
                  <label className="block text-gray-700 font-medium mb-1">
                    Catégorie de personnes concernées
                  </label>
                  <select
                    value={category}
                    onChange={(e) => setCategory(e.target.value)}
                    className="w-full p-2 border rounded-md bg-white"
                  >
                    <option value="Employé">Employé</option>
                    <option value="Client">Client</option>
                    <option value="Sous-traitant">Sous-traitant</option>
                    <option value="Candidat">Candidat</option>
                    <option value="Prospect">Prospect</option>
                    <option value="Tiers">Tiers</option>
                  </select>
                </div>

                {/* Date Input */}
                <div>
                  <label className="block text-gray-700 font-medium mb-1">
                    Date
                  </label>
                  <input
                    type="date"
                    value={date}
                    onChange={(e) => setDate(e.target.value)}
                    className="w-full p-2 border rounded-md bg-white"
                  />
                </div>

                {/* Version Input */}
                <div>
                  <label className="block text-gray-700 font-medium mb-1">
                    Version
                  </label>
                  <input
                    type="text"
                    value={version}
                    onChange={(e) => setVersion(e.target.value)}
                    className="w-full p-2 border rounded-md bg-white"
                  />
                </div>
              </div>

              {/* Utiliser un template button correctly placed on second line */}
              <div className="mt-4 flex flex-col items-start">
                <button className="bg-gray-200 text-gray-700 px-4 py-2 rounded-lg flex items-center gap-2 hover:bg-gray-300">
                  Utiliser un template existant
                  <ChevronDown size={18} />
                </button>
              </div>
            </div>
          )}

          {/* Section: Content Area */}
          {activeTab.mainTab === "notices" && activeTab.subTab === "creation" && (
            <div className="bg-white p-6 mt-4 shadow-md rounded-lg">
              <div className="grid grid-cols-[2fr_2fr] gap-2">
                {/* French Version */}
                <div className="p-4 border rounded-lg bg-gray-50">
                  <h3 className="font-semibold text-blue-600 mb-2">
                    Version française
                  </h3>
                  <textarea
                    className="w-full h-40 p-3 border rounded-md bg-white text-sm"
                    defaultValue="Al Salam Bank Algeria met en place une politique axée sur la protection de la vie privée..."
                  />
                </div>

                {/* Arabic Version */}
                <div className="p-4 border rounded-lg bg-gray-50">
                  <h3 className="font-semibold text-blue-600 mb-2">
                    Version arabe
                  </h3>
                  <textarea
                    className="w-full h-40 p-3 border rounded-md bg-white text-right text-sm"
                    defaultValue="بنك السلام الجزائر يضع سياسة تركز على حماية الحياة الخاصة..."
                  />
                </div>
              </div>

              {/* Save & Export Buttons */}
              <div className="flex justify-end mt-4 space-x-4">
                <button className="flex items-center bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">
                  <Save className="mr-2" size={18} /> Enregistrer
                </button>
                <button className="flex items-center bg-gray-300 text-gray-700 px-4 py-2 rounded-lg hover:bg-gray-400">
                  <FileUp className="mr-2" size={18} /> Exporter
                </button>
              </div>
            </div>
          )}

          {/* Other Tabs Content */}
          {activeTab.mainTab === "notices" && activeTab.subTab === "diffusion" && (
            <p>📢 Diffusion content goes here...</p>
          )}

          {activeTab.mainTab === "notices" && activeTab.subTab === "archivage" && (
            <p>📁 Archivage content goes here...</p>
          )}

          {activeTab.mainTab === "gestion" && (
            <p>📊 Gestion et suivi des consentements content goes here...</p>
          )}
        </div>
      </div>
    </div>
  );
}
