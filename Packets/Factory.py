from Packets.Messages.Client.ClientHelloMessage import ClientHelloMessage
from Packets.Messages.Client.LoginMessage import LoginMessage
from Packets.Messages.Client.AllianceChatMessage import AllianceChatMessage
from Packets.Messages.Client.KeepAliveMessage import KeepAliveMessage
from Packets.Messages.Client.TeamCreateMessage import TeamCreateMessage
from Packets.Messages.Client.GoHomeFromOfflinePractiseMessage import GoHomeFromOfflinePractiseMessage
from Packets.Messages.Client.TeamLeaveMessage import TeamLeaveMessage
from Packets.Messages.Client.AskProfileMessage import AskProfileMessage
from Packets.Messages.Client.AskForAllianceDataMessage import AskForAllianceDataMessage
from Packets.Messages.Client.TeamSetLocationMessage import TeamSetLocationMessage
from Packets.Messages.Client.TeamChangeMemberSettingsMessage import TeamChangeMemberSettingsMessage
from Packets.Messages.Client.AnalyticsEventMessage import AnalyticsEventMessage
from Packets.Messages.Client.BattleEndMessage import BattleEndMessage
from Packets.Messages.Client.SetNameMessage import SetNameMessage
from Packets.Messages.Client.SetContentCreatorMessage import SetContentCreatorMessage
from Packets.Messages.Client.AvatarNameCheckRequestMessage import AvatarNameCheckRequestMessage
from Packets.Messages.Client.TeamUseGadgetMessage import TeamUseGadgetMessage
from Packets.Messages.Client.DoNotDistrubMessage import DoNotDistrubMessage
from Packets.CommandFactory import EndClientTurn

packets = {
    10100: ClientHelloMessage,
    10101: LoginMessage,
    10108: KeepAliveMessage,
    10110: AnalyticsEventMessage,
    18686: SetContentCreatorMessage,
    10212: SetNameMessage,
    14102: EndClientTurn,
    14109: GoHomeFromOfflinePractiseMessage,
    14110: BattleEndMessage,
    14113: AskProfileMessage,
    14302: AskForAllianceDataMessage,
    14315: AllianceChatMessage,
    14350: TeamCreateMessage,
    14353: TeamLeaveMessage,
    14363: TeamSetLocationMessage,
    14354: TeamChangeMemberSettingsMessage,
    14372: TeamUseGadgetMessage,
    14600: AvatarNameCheckRequestMessage,
    14777: DoNotDistrubMessage,

}
