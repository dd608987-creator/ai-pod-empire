import React from "react";
import MetricCard from "./components/MetricCard";
import ChartCard from "./components/ChartCard";
import PlatformScalingCard from "./components/PlatformScalingCard";

export default function Dashboard() {
  return (
    <div className="p-6 bg-gray-900 min-h-screen text-white">
      <h1 className="text-4xl font-bold mb-6">AI POD Empire Dashboard</h1>

      <div className="grid grid-cols-3 gap-6">
        <MetricCard title="Brain Status" value="Running" />
        <MetricCard title="Latest Publish" value="TikTok: Success" />
        <MetricCard title="Scaling Up" value="TikTok" />
      </div>

      <div className="grid grid-cols-2 gap-6 mt-6">
        <ChartCard />
        <PlatformScalingCard />
      </div>
    </div>
  );
}
