"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

export default function SidebarItem({ icon: Icon, text, href }) {
  const pathname = usePathname();
  const isActive = pathname === href;

  return (
    <Link href={href} className="w-full">
      <div
        className={`flex items-center space-x-3 p-2 cursor-pointer ${
          isActive ? "text-blue-600 font-semibold" : "text-gray-800 hover:text-blue-600"
        }`}
      >
        <Icon className="w-5 h-5" />
        <span className="text-sm font-medium">{text}</span>
      </div>
    </Link>
  );
}