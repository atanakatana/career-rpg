import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { Badge } from "@/components/ui/badge";
import { Shield, Brain, Zap, Target, Heart } from "lucide-react";

// Dummy data structure reflecting API response
const charData = {
  name: "Alex",
  level: 1,
  character_class: "The Data Catalyst",
  archetype_desc: "A visionary who bridges the gap between raw logic and human empathy, excelling in environments that require strategic foresight.",
  stats: { wisdom: 85, leadership: 60, creativity: 75, empathy: 90, execution: 70 },
  quests: [
    { title: "AI Product Manager", difficulty: "Hard", income_potential: "High", ai_resistance: "High", why_you: "Your Projector HD type gives you natural guidance abilities, while your INTJ logic aligns with AI systems.", required_skills: "Product Strategy, AI Ethics, Stakeholder Management" }
  ]
};

export default function Dashboard() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-50 p-8 font-sans">
      <header className="mb-8 flex justify-between items-center border-b border-slate-800 pb-4">
        <div>
          <h1 className="text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-500">
            {charData.name}'s Character Sheet
          </h1>
          <p className="text-xl text-slate-400">Level {charData.level} • {charData.character_class}</p>
        </div>
        <button className="bg-slate-800 hover:bg-slate-700 px-4 py-2 rounded-md transition">
          Export PDF
        </button>
      </header>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        
        {/* Left Column: Stats */}
        <div className="space-y-6">
          <Card className="bg-slate-900 border-slate-800 text-slate-100">
            <CardHeader>
              <CardTitle className="text-lg flex items-center gap-2">
                <Brain className="w-5 h-5 text-purple-400"/> Primary Stats
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <StatRow icon={<Brain size={16}/>} label="Wisdom" value={charData.stats.wisdom} color="bg-blue-500" />
              <StatRow icon={<Shield size={16}/>} label="Leadership" value={charData.stats.leadership} color="bg-yellow-500" />
              <StatRow icon={<Zap size={16}/>} label="Creativity" value={charData.stats.creativity} color="bg-purple-500" />
              <StatRow icon={<Heart size={16}/>} label="Empathy" value={charData.stats.empathy} color="bg-green-500" />
              <StatRow icon={<Target size={16}/>} label="Execution" value={charData.stats.execution} color="bg-red-500" />
            </CardContent>
          </Card>

          <Card className="bg-slate-900 border-slate-800 text-slate-100">
            <CardHeader>
              <CardTitle className="text-lg text-emerald-400">Core Identity</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-sm text-slate-300 leading-relaxed">
                {charData.archetype_desc}
              </p>
            </CardContent>
          </Card>
        </div>

        {/* Right Column: Quest Board */}
        <div className="col-span-2 space-y-6">
          <h2 className="text-2xl font-bold border-b border-slate-800 pb-2">Career Quest Board</h2>
          <div className="grid grid-cols-1 gap-4">
            {charData.quests.map((quest, idx) => (
              <Card key={idx} className="bg-slate-900 border-slate-700 hover:border-blue-500 transition-colors text-slate-100">
                <CardHeader>
                  <div className="flex justify-between items-start">
                    <CardTitle className="text-xl text-blue-400">{quest.title}</CardTitle>
                    <Badge variant="outline" className="text-xs border-amber-500 text-amber-500">
                      Difficulty: {quest.difficulty}
                    </Badge>
                  </div>
                </CardHeader>
                <CardContent className="space-y-4">
                  <div className="flex gap-4 text-sm">
                    <span className="bg-slate-800 px-2 py-1 rounded">💰 Income: {quest.income_potential}</span>
                    <span className="bg-slate-800 px-2 py-1 rounded">🛡️ AI Resistance: {quest.ai_resistance}</span>
                  </div>
                  <div>
                    <h4 className="text-sm font-semibold text-slate-400 mb-1">Why You?</h4>
                    <p className="text-sm text-slate-300">{quest.why_you}</p>
                  </div>
                  <div>
                    <h4 className="text-sm font-semibold text-slate-400 mb-2">Required Skills</h4>
                    <div className="flex flex-wrap gap-2">
                      {quest.required_skills.split(',').map((skill, sIdx) => (
                        <Badge key={sIdx} className="bg-slate-800 hover:bg-slate-700">{skill.trim()}</Badge>
                      ))}
                    </div>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>

      </div>
    </div>
  );
}

function StatRow({ icon, label, value, color }: { icon: React.ReactNode, label: string, value: number, color: string }) {
  return (
    <div>
      <div className="flex justify-between text-sm mb-1 text-slate-400">
        <span className="flex items-center gap-2">{icon} {label}</span>
        <span>{value}/100</span>
      </div>
      {/* Custom Progress bar styling using shadcn */}
      <div className="w-full bg-slate-800 rounded-full h-2 overflow-hidden">
        <div
          className={`h-full ${color} transition-all duration-300`}
          style={{ width: `${value}%` }}
        />
      </div>
    </div>
  );
}