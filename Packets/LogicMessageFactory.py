from Packets.Messages.Client.Login.ClientHelloMessage import ClientHelloMessage
from Packets.Messages.Client.Login.LoginMessage import LoginMessage
from Packets.Messages.Client.Alliance.ChatToAllianceStreamMessage import ChatToAllianceStreamMessage
from Packets.Messages.Client.KeepAliveMessage import KeepAliveMessage
from Packets.Messages.Client.Gameroom.TeamCreateMessage import TeamCreateMessage
from Packets.Messages.Client.Battle.GoHomeFromOfflinePractiseMessage import GoHomeFromOfflinePractiseMessage
from Packets.Messages.Client.Gameroom.TeamLeaveMessage import TeamLeaveMessage
from Packets.Messages.Client.Home.AskProfileMessage import AskProfileMessage
from Packets.Messages.Client.Alliance.AskForAllianceDataMessage import AskForAllianceDataMessage
from Packets.Messages.Client.Gameroom.TeamSetLocationMessage import TeamSetLocationMessage
from Packets.Messages.Client.Gameroom.TeamChangeMemberSettingsMessage import TeamChangeMemberSettingsMessage
from Packets.Messages.Client.AnalyticsEventMessage import AnalyticsEventMessage
from Packets.Messages.Client.Battle.AskForBattleEndMessage import AskForBattleEndMessage
from Packets.Messages.Client.SetNameMessage import SetNameMessage
from Packets.Messages.Client.Home.GetLeaderboardMessage import GetLeaderboardMessage
from Packets.Messages.Client.Home.AvatarNameCheckRequestMessage import AvatarNameCheckRequestMessage
from Packets.Messages.Client.Gameroom.TeamUseGadgetMessage import TeamUseGadgetMessage
from Packets.Messages.Client.Gameroom.Do_Not_Distrub_Message import DoNotDistrubMessage
from Packets.Messages.Client.Home.PlayerStatusMessage import PlayerStatusMessage
from Packets.LogicCommandManager import EndClientTurn

packets = {
    10100: ClientHelloMessage,
    10101: LoginMessage,
    10108: KeepAliveMessage,
    10110: AnalyticsEventMessage,
    10212: SetNameMessage,
    14102: EndClientTurn,
    14109: GoHomeFromOfflinePractiseMessage,
    14110: AskForBattleEndMessage,
    14113: AskProfileMessage,
    14403: GetLeaderboardMessage,
    14302: AskForAllianceDataMessage,
    14315: ChatToAllianceStreamMessage,
    14350: TeamCreateMessage,
    14353: TeamLeaveMessage,
    14363: TeamSetLocationMessage,
    14354: TeamChangeMemberSettingsMessage,
    14372: TeamUseGadgetMessage,
    14600: AvatarNameCheckRequestMessage,
    14366: PlayerStatusMessage,
    14777: DoNotDistrubMessage,

}
