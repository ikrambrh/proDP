import SidebarItem from "./SidebarItem";
import { 
  Layers, Users, CheckSquare, Handshake, FileText, Shield, GraduationCap, BarChart, Book 
} from "lucide-react";

export default function Sidebar() {
    return (
      <div className="w-64 h-screen bg-white shadow-md flex flex-col p-3 overflow-hidden">
        {/* Logo */}
        <div className="flex justify-start items-start mb-6 px-6 py-2">
          <img src="/images/logo.png" alt="proDP Logo" className="h-10" />
        </div>
  
        {/* Navigation Links */}
        <nav className="flex flex-col space-y-4 flex-grow overflow-hidden">
          <SidebarItem icon={Layers} text="Traitements" href="../traitements" />
          <SidebarItem icon={Users} text="Exercice de droits" href="/droits" />
          <SidebarItem icon={CheckSquare} text="Consentements" href="/consentements" />
          <SidebarItem icon={Handshake} text="Sous-traitance" href="/sous-traitance" />
          <SidebarItem icon={FileText} text="Audit de conformité" href="/audit" />
          <SidebarItem icon={Shield} text="Incidents" href="/incidents" />
          <SidebarItem icon={GraduationCap} text="Formations" href="/formations" />
          <SidebarItem icon={BarChart} text="Tableau de bord" href="/dashboard" />
          <SidebarItem icon={Book} text="Ressources juridiques" href="/ressources" />
        </nav>
      </div>
    );
  }
  