import { useState } from "react";
import { Search, Bell, ChevronDown, Menu, Settings, LogOut } from "lucide-react";

export default function TopBar() {
  const [showNotifications, setShowNotifications] = useState(false);
  const [showProfileMenu, setShowProfileMenu] = useState(false);

  // Example notifications
  const notifications = [
    "📢 Nouvelle mise à jour disponible",
    "✅ Votre tâche a été validée",
    "⚠️ Alerte de sécurité détectée",
  ];

  return (
    <div className="flex items-center justify-between bg-white shadow-md p-4 relative">
      {/* Left: Menu + Search Bar */}
      <div className="flex items-center gap-4">
        <Menu className="w-6 h-6 cursor-pointer" />
        <div className="relative w-96">
          <Search className="absolute left-3 top-2.5 text-gray-400 w-4 h-4" />
          <input
            type="text"
            placeholder="Recherche"
            className="w-full pl-10 pr-4 py-2 rounded-full bg-gray-100 focus:outline-none focus:ring-2 focus:ring-blue-500"
          /> 
        </div>
      </div>

      {/* Right: Notification Bell + Profile */}
      <div className="flex items-center gap-6">
        {/* Notification Bell */}
        <div className="relative cursor-pointer" onClick={() => setShowNotifications(!showNotifications)}>
          <Bell className="w-6 h-6 text-gray-600" />
          
          {/* Show red dot only if there are notifications */}
          {notifications.length > 0 && (
            <span className="absolute top-0 right-0 w-2.5 h-2.5 bg-red-500 rounded-full"></span>
          )}

          {/* Dropdown Notifications */}
          {showNotifications && (
            <div className="absolute right-0 mt-2 w-64 bg-white shadow-lg rounded-lg p-4">
              <p className="text-sm font-semibold">Notifications</p>
              <ul className="mt-2">
                {notifications.map((notif, index) => (
                  <li key={index} className="p-2 text-gray-700 hover:bg-gray-100 rounded-md cursor-pointer">
                    {notif}
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>

        {/* Profile Section */}
        <div className="relative">
          <div 
            className="flex items-center gap-2 cursor-pointer"
            onClick={() => setShowProfileMenu(!showProfileMenu)}
          >
            <div className="w-10 h-10 rounded-full bg-gray-200 flex items-center justify-center">
              <span className="text-gray-600 text-xl">👤</span>
            </div>
            <div>
              <p className="text-sm font-semibold">Azyadi</p>
              <p className="text-xs text-blue-600">Collaborateur Mazars</p>
            </div>
            <ChevronDown className="w-4 h-4 text-gray-600" />
          </div>

          {/* Profile Dropdown */}
          {showProfileMenu && (
            <div className="absolute right-0 mt-2 w-48 bg-white shadow-lg rounded-lg py-2">
              <button className="flex items-center gap-2 w-full px-4 py-2 text-gray-700 hover:bg-gray-100">
                <Settings className="w-5 h-5" />
                Paramètres
              </button>
              <button className="flex items-center gap-2 w-full px-4 py-2 text-gray-700 hover:bg-gray-100">
                <LogOut className="w-5 h-5" />
                Se déconnecter
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
