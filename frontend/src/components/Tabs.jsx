"use client";

import { useState } from "react";

export default function Tabs({ tabs, onTabChange }) {
  const [activeMainTab, setActiveMainTab] = useState(tabs[0]?.key);
  const [activeSubTab, setActiveSubTab] = useState(
    tabs[0]?.subTabs?.[0]?.key || null
  );

  const handleMainTabClick = (key) => {
    setActiveMainTab(key);
    const subTabs = tabs.find((tab) => tab.key === key)?.subTabs;
    if (subTabs && subTabs.length > 0) {
      setActiveSubTab(subTabs[0].key);
    } else {
      setActiveSubTab(null);
    }
    onTabChange({ mainTab: key, subTab: subTabs ? subTabs[0]?.key : null });
  };

  const handleSubTabClick = (key) => {
    setActiveSubTab(key);
    onTabChange({ mainTab: activeMainTab, subTab: key });
  };

  return (
    <div>
      {/* Main Tabs */}
      <div className="flex w-full border-b-2 border-gray-300 bg-white">
        {tabs.map((tab) => (
          <button
            key={tab.key}
            onClick={() => handleMainTabClick(tab.key)}
            className={`flex-1 text-center py-3 font-semibold text-base transition ${
              activeMainTab === tab.key
                ? "border-b-4 border-blue-600 text-blue-600"
                : "text-gray-500"
            }`}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {/* Sub-tabs (if applicable) */}
      {tabs.find((tab) => tab.key === activeMainTab)?.subTabs && (
        <div className="flex w-full border-b border-gray-300 bg-white font-medium">
          {tabs
            .find((tab) => tab.key === activeMainTab)
            ?.subTabs?.map((subTab) => (
              <button
                key={subTab.key}
                onClick={() => handleSubTabClick(subTab.key)}
                className={`flex-1 text-center py-2 transition ${
                  activeSubTab === subTab.key
                    ? "border-b-2 border-blue-600 text-blue-600"
                    : "text-gray-500"
                }`}
              >
                {subTab.label}
              </button>
            ))}
        </div>
      )}
    </div>
  );
}
