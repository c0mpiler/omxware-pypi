import omxware

testTKN = '3bpNkguJSIK5HCrN3u4qFoEUmOyRDLaQOhN4DOspdgJXfOIiul6omJclxc3WTtmoH7rCcUYoevTeGUelndSxCHlP1HaCB09Rd84mwRAytS0wv3a6vh+BITKZT0cq+6DJ'

token = 'U+capXJnM6zRtTdgub8sbN9sjiE6vg9JYkxotXdNxxBCbBFcoFCYfMqhk6uqho+fiFg5qTHNcezkKkPQxOnyc7Zq5XOn2WjxrlcelWARfAk='

omx = omxware.omxware(token)
# omx = omxware(testTKN, env='local')

# genera = omx.genus(genus_names='vibrio,salmonella,klebsiella')
# genus_lst = ['vibrio','salmonella','klebsiella']
#
# genera1 = omx.genus(genus_names=genus_lst)
#
# print(genera)
#
# genomes = omx.genomes(genus_names='vibrio,mesorhizobium', genome_ids='ERR1595603,ERR570089')
# dframe = genomes.results(type='df')
#
# print("\n\n\n")
# print(dframe)
#
# genes = omx.genes(genus_names='vibrio,mesorhizobium', genome_ids='ERR1595603,ERR570089', page_size=3)
# dframe = genes.results(type='df')
# print("\n\n\n")
# print(dframe)
#
# dframe = genera.results(type='df')
# print("\n\n\n")
# print(dframe)

# print("\n\n\n")
# x = omx.domains(ids='eb19229d99985df36c0a59bfc89b507e')
# domain1 = x.results()[0]
# print(domain1.get_id())
# print(domain1.get_type())

# genus = genera.results()[0]

# genomes_for_genus = genus.get_genomes().results()
# genes_for_genus = genus.genes().results()
# proteins_for_genus = genus.proteins().results()
# domains_for_genus = genus.domains().results()

# print(genomes_for_genus)
# print(genes_for_genus)
# print(proteins_for_genus)
# print(domains_for_genus)

# print(genomes_for_genus[0].id())
# print(genomes_for_genus[0].metadata(type='biosample'))

# genes = omx.genes(genome_ids='GCF_001141225.1', page_size=1)
# gene = genes.results()[0]
# print(gene.genomes())

# genome = omx.genomes(ids="GCF_001141225.1").results()[0]
# print(genome.genus())

# user = omx.whoami()
# user = user.results()[0]
# print(user._isAdmin())
# print(user._role(omx_role='omxware-team'))

# protein = omx.proteins(ids='6a2286bcd8900ddcc9dc34bf010f50aa,000421c1f91b290085933cd642364a6f')
# protein_fasta = protein.results(type='fasta')
#
# print(protein_fasta + "\n\n")
#
# protein_etty = protein.results()[0]
#
# domains = protein_etty.domains().results()
# print(domains[0])


# genes = omx.genes(ids='921db25406f80e09c8f78dd915f355aa')
# genes = genes.results()
#
# gene = genes[0]
# # print(gene)
#
# res = gene.go().results()[0]
# print(res)


# genome_id = 'SRR3314498'
#
# genomes = omx.genomes(ids=genome_id)
# genome = genomes.results()[0]
#
# # For the Genome ^^^^^^^^^^^
# id = genome.id()
# typ = genome.genome_type()
# taxid = genome.taxid()
# metadata = genome.metadata('biosample')
#
# genera = genome.genus().results()
#
# print('ID: ' + id)
# print('Type: ' + typ)
# print('TaxID: ' + taxid)
# print('BioSample: ' + str(metadata))
# print('Genera: ' + str(genera))
#
# # print(genome.file())
#
# search_string = 'sporulation'
# response = omx.genes(gene_name=search_string, page_size=25)
# response.show_facets(name='genera', topN=7)

r = omx.genomes(genus_names='salmonella', page_size=6, created_after='2018-02', created_before='2018-03-01')
l = len(r.results())
print(l)

print(r.results()[0])
