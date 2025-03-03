import Link from "next/link";

export default function SidebarItem({ icon: Icon, text, href }) {
  return (
    <Link href={href}>
      <div className="flex items-center space-x-3 text-gray-800 hover:text-blue-600 cursor-pointer p-2">
        <Icon className="w-5 h-5" />
        <span className="text-sm font-medium">{text}</span>
      </div>
    </Link>
  );
}
