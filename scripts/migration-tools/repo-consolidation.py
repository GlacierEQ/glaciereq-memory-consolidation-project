#!/usr/bin/env python3
"""
Repository Consolidation Script
Automated migration tool for GlacierEQ memory ecosystem
"""

import os
import subprocess
import json
from pathlib import Path
from typing import List, Dict

class RepoConsolidator:
    def __init__(self, config_path: str = 'consolidation-config.json'):
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        
        self.master_repo = self.config['master_repo']
        self.source_repos = self.config['source_repos']
        self.github_org = self.config['github_org']
    
    def create_master_repo(self):
        """Create the master repository structure"""
        print(f"🚀 Creating master repository: {self.master_repo}")
        
        # Create directory structure
        directories = [
            'core/memory-orchestrator',
            'core/master-grid', 
            'core/constellation',
            'core/quantum-matrix',
            'graph/mem0-integration',
            'graph/neo4j-providers',
            'graph/supermemory-bridge',
            'graph/vector-operations',
            'orchestration/mcp-hub',
            'orchestration/apex-orchestrator',
            'connectors/google-drive',
            'connectors/notion-engine',
            'specialized/desktop-commander',
            'specialized/deadline-tracker',
            'workspace/notion-optimizer',
            'enterprise/n8n-integration',
            'api-bridges/fileboss-bridge',
            'api-bridges/omni-engine-bridge'
        ]
        
        for directory in directories:
            Path(directory).mkdir(parents=True, exist_ok=True)
            print(f"  ✅ Created {directory}")
    
    def migrate_repository(self, repo_name: str, target_path: str):
        """Migrate a repository using git subtree to preserve history"""
        print(f"📦 Migrating {repo_name} to {target_path}")
        
        try:
            # Add remote
            subprocess.run([
                'git', 'remote', 'add', f'{repo_name}-remote',
                f'https://github.com/{self.github_org}/{repo_name}.git'
            ], check=True)
            
            # Fetch repository
            subprocess.run([
                'git', 'fetch', f'{repo_name}-remote'
            ], check=True)
            
            # Add as subtree
            subprocess.run([
                'git', 'subtree', 'add', '--prefix', target_path,
                f'{repo_name}-remote', 'main', '--squash'
            ], check=True)
            
            print(f"  ✅ Successfully migrated {repo_name}")
            
        except subprocess.CalledProcessError as e:
            print(f"  ❌ Failed to migrate {repo_name}: {e}")
    
    def create_integration_config(self):
        """Create integration configuration files"""
        print("⚙️ Creating integration configuration")
        
        # MCP servers configuration
        mcp_config = {
            "mcpServers": {
                "memory-orchestrator": {
                    "command": "python",
                    "args": ["core/memory-orchestrator/server.py"],
                    "env": {
                        "NEO4J_URI": "bolt://localhost:7687",
                        "SUPERMEMORY_API_KEY": "${SUPERMEMORY_API_KEY}"
                    }
                },
                "master-grid": {
                    "command": "python",
                    "args": ["core/master-grid/server.py"]
                }
            }
        }
        
        with open('mcp-servers.json', 'w') as f:
            json.dump(mcp_config, f, indent=2)
        
        # Docker compose for dependencies
        docker_compose = """
version: '3.8'
services:
  neo4j:
    image: neo4j:latest
    environment:
      - NEO4J_AUTH=neo4j/password
      - NEO4J_PLUGINS=["apoc"]
    ports:
      - "7474:7474"
      - "7687:7687"
    volumes:
      - neo4j_data:/data
      - neo4j_logs:/logs
      - neo4j_import:/var/lib/neo4j/import
      - neo4j_plugins:/plugins
    
  chromadb:
    image: chromadb/chroma:latest
    ports:
      - "8000:8000"
    volumes:
      - chroma_data:/chroma/chroma

volumes:
  neo4j_data:
  neo4j_logs:
  neo4j_import:
  neo4j_plugins:
  chroma_data:
"""
        
        with open('docker-compose.yml', 'w') as f:
            f.write(docker_compose)
        
        print("  ✅ Created integration configuration files")
    
    def run_consolidation(self):
        """Run the complete consolidation process"""
        print("🎯 Starting GlacierEQ Memory Consolidation")
        print("="*50)
        
        # Create master repository structure
        self.create_master_repo()
        
        # Migrate repositories by phase
        phases = {
            'Phase 1 - Critical Core': [
                ('quantum-memory-orchestrator', 'core/memory-orchestrator'),
                ('MCP-MASTER-OMNI-GRID', 'core/master-grid'),
                ('casey-custom-mcp-constellation', 'core/constellation'),
                ('GODMIND-quantum-intelligence-matrix', 'core/quantum-matrix')
            ],
            'Phase 2 - Graph Memory': [
                ('mem0-powerhouse', 'graph/mem0-integration'),
                ('smithery-mcp-ultimate-v2', 'graph/production-scaffold'),
                ('perplexity-voice-integration', 'graph/supermemory-bridge'),
                ('constellation-memory-engine', 'graph/constellation-engine')
            ]
        }
        
        for phase_name, repos in phases.items():
            print(f"\n🚀 {phase_name}")
            print("-" * 30)
            
            for repo_name, target_path in repos:
                self.migrate_repository(repo_name, target_path)
        
        # Create integration configuration
        self.create_integration_config()
        
        print("\n🎉 Consolidation Complete!")
        print("Next steps:")
        print("1. Review migrated code")
        print("2. Update import statements")
        print("3. Test integration")
        print("4. Run docker-compose up for dependencies")

if __name__ == '__main__':
    consolidator = RepoConsolidator()
    consolidator.run_consolidation()