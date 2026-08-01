import { useEffect, useState } from "react";

interface DashboardUser {
  full_name: string;
  email: string;
}

function getStoredUser(): DashboardUser | null {
  const userJson = localStorage.getItem("user");
  return userJson ? JSON.parse(userJson) : null;
}

export default function Dashboard() {
  const [user] = useState<DashboardUser | null>(getStoredUser);

  useEffect(() => {
    if (!user) {
      window.location.href = "/login";
    }
  }, [user]);

  const handleLogout = () => {
    localStorage.removeItem("accessToken");
    localStorage.removeItem("refreshToken");
    localStorage.removeItem("user");
    window.location.href = "/login";
  };

  if (!user) {
    return null;
  }

  return (
    <div className="min-h-screen bg-slate-50 px-4 py-12">
      <div className="mx-auto max-w-2xl">
        <div className="flex items-center justify-between rounded-2xl bg-white p-8 shadow-sm ring-1 ring-slate-200">
          <div>
            <h1 className="text-2xl font-semibold text-slate-900">
              Hello, {user.full_name || user.email}
            </h1>
            <p className="mt-1 text-sm text-slate-500">This is your profile</p>
          </div>

          <button
            onClick={handleLogout}
            className="rounded-lg border border-slate-300 px-4 py-2 text-sm font-medium text-slate-700 hover:bg-slate-50"
          >
            Log out
          </button>
        </div>

        <div className="mt-6 rounded-2xl bg-white p-8 shadow-sm ring-1 ring-slate-200">
          <h2 className="text-sm font-medium text-slate-500">Email</h2>
          <p className="mt-1 text-slate-900">{user.email}</p>
        </div>
      </div>
    </div>
  );
}